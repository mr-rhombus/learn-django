from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django.forms import ModelForm
from basic_app import models

class CreateSchoolForm(ModelForm):
    class Meta:
        model = models.School
        fields = ('name', 'principal', 'location')
    
    # Only needed when using {% crispy form %} tag
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.add_input(Submit('submit', 'Submit'))