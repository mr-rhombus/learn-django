from django.shortcuts import render

# Create your views here.
def help(request):
    help_dict = {'insert_help': 'HEEEELLPPPP!'}
    return render(request, 'help/index.html', context=help_dict)