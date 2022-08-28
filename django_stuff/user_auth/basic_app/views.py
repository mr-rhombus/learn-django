from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    # Assume user is not registered
    registered = False
    # POST request
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        if profile_form.is_valid():
            # user form
            user = user_form.save()
            user.set_password(user.password)  # hash the password
            user.save()
            # profile form
            # Get profile info from form, but don't commit yet so we don't get collision errors by trying to save over existing user in user_form
            profile = profile_form.save(commit=False)
            profile.user = user
            # request.FILES is a dict of files a user uploads during the request
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print('invalid')
            # print(user_form.errors, profile_form.errors)  # print out the errors for the form(s)
            print(profile_form.errors)
    # HTTP request
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request, 'basic_app/register.html', 
            {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered,
            })


def login(request):
    return render(request, 'basic_app/login.html')