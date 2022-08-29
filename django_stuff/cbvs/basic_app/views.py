from pipes import Template
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from typing import Any, Dict
from basic_app import models, forms
from django.urls import reverse_lazy

# Create your views here.
## Function-based view
# def index(request):
#     return render(request, 'index.html')

## Class-based view
class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'Basic injection :)'
    #     return context

class SchoolListView(ListView):
    model = models.School
    # Define the "list" context_dict returned by ListView
    context_object_name = 'schools'
    # If we don't define context_object_name, the ListView returns a list called school_list (lowercase of model name + "_list")
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    # If we don't define context_object_name, the DetailView returns a context dict called school (lowercase of model name)
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    # fields = ('name', 'principal', 'location')
    form_class = forms.CreateSchoolForm
    # template_name = 'basic_app/create_school.html'
    ## default template_name is 'basic_app/school_form.html'

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    # Once you successfully delete, go back to school list view
    # Evaluated lazily since we only want it eval'd when called
    success_url = reverse_lazy('basic_app:school_list')