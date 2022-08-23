from django.shortcuts import render
from signup.forms import SignupForm
from django.core.exceptions import ValidationError

# Create your views here.
def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                form.full_clean()
                form.save()
            except:
                raise ValidationError('Please enter an email that is not already aligned to an account!')

    return render(request, 'signup/signup.html', {'form': form})