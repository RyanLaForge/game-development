__author__ = 'rlaforge'


from webapp2 import Route

routes = [
    Route('/portfolio/login', name='portfolio-login', handler='app.handlers.portfolio.login_handler.LoginHandler')
]