from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('slaking', views.favorite_pkmn, name='favorite pokemon'),
    path('users', views.users, name='users')
]