__author__ = 'Ryan'
from main import jinja_env
import webapp2

class BaseHandler(webapp2.RequestHandler):
    """This class will handle the actions that need to be performed by all handlers.
        This includes convenience methods.

    """
    def render_template(self, template, **kwargs):
        """Writes the given template to the handler output.
        :param: template:basestring: The name of the html template in the templates directory.
        :param: kwargs: Named arguments that can be referenced by name on the html page
        :postcon: The template is written and displayed to the user.
        """
        self.write(self.render_str(template, **kwargs))


    def render_str(self, template, **kwargs):
        """Render the template with the given arguments.
        :param: template:basestring: The name of the template in the templates directory.
        :param: kwargs:named variables to be used on the page.
        :return: The template rendered with the named arguments.
        """
        template = jinja_env.get_template(template)
        return template.render(**kwargs)


    def write(self, string, **kwargs):
        """Write the given string to output.
        :param: string: The string to write to the user.
        :param: kwargs: the names arguments to use.
        :postcon: The string is written to the user."""
        self.response.out.write(string, **kwargs)