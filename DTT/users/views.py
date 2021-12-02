from django.shortcuts import render
from django.contrib.auth.views import LoginView as DefaultLoginView, LogoutView as DefaultLogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LoginView(DefaultLoginView):
    pass


class LogoutView(DefaultLogoutView):
    pass


class PreferencesView(LoginRequiredMixin, FormView):
    pass
