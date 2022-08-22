from django.shortcuts import render
from django.http import HttpResponse
from . import signup_form

# Create your views here.
def signup(request):
    form = signup_form.SignupForm()

    if request.method == 'POST':
        form = signup_form.SignupForm(request.POST)
        if form.is_valid():
            # form.save()
            print('Validation successful!')
            print('Email:\t', form.cleaned_data['email'])
            print('Password:\t', form.cleaned_data['password'])


    return render(request, 'signup/signup.html', {'form': form})