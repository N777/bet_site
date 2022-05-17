from django_registration.forms import RegistrationForm

from stavki.models import Users


class MyCustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = Users
