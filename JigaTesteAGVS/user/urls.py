from django.urls import path
from .views import CustomLoginView, LogoutInterfaceView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutInterfaceView.as_view(), name='logout'),
]