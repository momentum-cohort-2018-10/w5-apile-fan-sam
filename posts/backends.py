from registration.backends.simple.views import RegistrationView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView


class HomeRegistrationView(SuccessMessageMixin, RegistrationView):
    success_url = 'home'
    success_message = "Registration Successful!"


class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Successfully Logged In!"
