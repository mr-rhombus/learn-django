from django.shortcuts import render
from . import forms

# Create your views here.

# Index, linked to templates
def index(request):
    return render(request, 'basicapp/index.html')


# Form name
def form_name_view(request):
    form = forms.FormName()
    # Do something with the data entered into the form
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():  # check validity of form
            print('Validation success!')
            print('Name:\t', form.cleaned_data['name'])
            print('Email:\t', form.cleaned_data['email'])
            print('Text:\t', form.cleaned_data['text'])

    # render request, html page name and context dict
    # render() takes the request obj as its first arg, a template name as its second arg and a dictionary as its (optional) third arg. It returns an HttpResponse object of the given template rendered with the given context.
    return render(request, 'basicapp/form_page.html', {'form': form})