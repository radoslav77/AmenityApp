from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.views.generic.edit import FormView

from .models import *


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# craete intoform // got the idea from https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
class DateInput(forms.DateInput):
    input_type = 'date'


class InputData(forms.ModelForm):

    class Meta:
        model = InputAmenity

        fields = '__all__'
        # change input to date input
        widgets = {
            'arrival_date': DateInput(),
            'checkout_date' : DateInput()
        }
