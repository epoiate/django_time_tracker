from django.urls import path
from .views import LoginView, LogoutView, PreferencesView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('preferences/', PreferencesView.as_view())
]