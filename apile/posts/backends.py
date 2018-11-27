from registration.backends.simple.views import RegistrationView


class HomeRegistrationView(RegistrationView):
    success_url = 'home'
