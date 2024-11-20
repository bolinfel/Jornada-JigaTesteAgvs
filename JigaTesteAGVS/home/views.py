from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

'''
class LogoutInterfaceView(LogoutView):
  template_name='logout.html'
'''

'''
class LoginInterfaceView(LoginView):
  template_name='login.html'
'''

class HomeView(LoginRequiredMixin, TemplateView):
  template_name = 'home.html'
  login_url = 'user/login/'  # URL da página de login

