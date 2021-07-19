from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    template_name = "login-form.html"


class UserLogoutView(LogoutView):
    next_page = "login"

class Home(TemplateView):
    template_name = "home.html"

