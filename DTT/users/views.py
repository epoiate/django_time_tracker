from django.shortcuts import render
from django.contrib.auth.views import LoginView as DefaultLoginView, LogoutView as DefaultLogoutView

# Create your views here.


class LoginView(DefaultLoginView):
    pass


class LogoutView(DefaultLogoutView):
    pass
