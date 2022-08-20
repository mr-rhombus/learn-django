from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic, Webpage, AccessRecord, User

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'AppTwo/index.html', context=date_dict)

    # my_dict = {'insert_me': 'Hello, I am from views.py in AppTwo! I populate AppTwo/index.html (:'}
    # return render(request, 'AppTwo/index.html', context=my_dict)

def favorite_pkmn(request):
    return render(request, 'AppTwo/favorite_pkmn.html')

def users(request):
    users_list = User.objects.all()
    user_dict = {'users': users_list}
    return render(request, 'AppTwo/users.html', context=user_dict)
