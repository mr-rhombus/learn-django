from django.urls import path
from basic_app import views

urlpatterns = [
    # path('', views.index, name='index')  # function-based view
    path('', views.CBView.as_view())  # class-based view
]