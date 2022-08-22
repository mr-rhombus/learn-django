from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from signup.models import NewUser

class SignupForm(forms.Form):
    class Meta:
        model = NewUser
        fields = '__all__'
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput())