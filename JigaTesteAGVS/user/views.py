from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

# Custom Login View (optional)
class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True  # Redirect logged-in users to the home page