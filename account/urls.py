from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView

from account.forms import MyCustomUserForm

urlpatterns = [
    path('register/',
         RegistrationView.as_view(
             form_class=MyCustomUserForm
         ),
         name='django_registration_register',
         ),
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]
