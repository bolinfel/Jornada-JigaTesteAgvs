from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class LogoutInterfaceView(LogoutView):
  template_name='logout.html'


class LoginInterfaceView(LoginView):
  template_name='login.html'


class HomeView(TemplateView):
  template_name = 'home.html'
