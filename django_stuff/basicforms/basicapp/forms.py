from xml.dom import ValidationErr
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

# Define your own validator
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise ValidationError('Name needs to start with z!')

class FormName(forms.Form):
    name = forms.CharField(
        # validators=[check_for_z]
    )
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    # Catch bots. Field won't show up on form
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

    ## Manual bot catcher
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     # Bots navigate to pages, open source code, and fill in vals for all form fields. If botcatcher has a value, we have a bot since a human won't see the botcatcher field
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha, bot!')
    #     return botcatcher

    # Clean the entire form at once
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        if email != v_email:
            raise ValidationError('Make sure your emails match!')