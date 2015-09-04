__author__ = 'Ryan'
from app.handlers.base_handler import BaseHandler
from app.models.user import User


class LoginHandler(BaseHandler):
    """Handler for the login page (initial screen load)."""
    def get(self):
        username = self.request.GET.get('username') or ""
        self.render_template('login.html', username=username)

    def post(self):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")

        errors = self.validate_form(username=username, password=password)
        if errors:
            self.render_template('login.html',
                                 username=username,
                                 **errors
                                 )
            return

        #TODO Move validating the user logic to the User model.
        #TODO Create a registration workflow.
        #TODO Add tests
        query = User.query(User.username==username)
        user = query.get()
        if not user:
            self.render_template('login.html', form_error='That username is not registered.')
            return
        elif user.password == password:
            self.write("THANKS BUD")
            return
        else:
            self.render_template('login.html', form_error='Wrong password for username %s' % username)

    def validate_form(self, username, password):
        username_error = password_error = ""
        if not username:
            username_error = "You must enter a username."
        verify_password = self.request.POST.get("verify-password")
        if not password:
            password_error = "You must supply a password!"
        elif not verify_password or (verify_password != password):
            password_error = "The two passwords must match."

        errors = {}
        if username_error:
            errors['username_error'] = username_error
        if password_error:
            errors['password_error'] = password_error

        return errors
