from django import forms
from signup.models import NewUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Enter login credentials!',
                'email',
                'password'
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )