from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    # path('', views.index, name='index')  # function-based view
    path('', views.IndexView.as_view(), name='index'),  # class-based view
    # path('school_detail', views.SchoolDetailView.as_view(), name='school_detail'),
    path('school_list', views.SchoolListView.as_view(), name='school_list'),
    # on school_list view, if we click a school we are linked to that school's detail view. Below, we define the primary key that aligns to the school, which is called from {{ school.id }} in school_list.html
    # path(r'school_detail/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school_detail'),
    path('school_detail/<int:pk>', views.SchoolDetailView.as_view(), name='school_detail'),
    # createview
    path('create_school', views.SchoolCreateView.as_view(), name='create_school'),
    # update view
    path('school_detail/<int:pk>/update', views.SchoolUpdateView.as_view(), name='update'),
    # delete view
    path('school_detail/<int:pk>/delete', views.SchoolDeleteView.as_view(), name='delete'),
]