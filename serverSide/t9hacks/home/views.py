from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from .models import *

from .forms import UserForm

# Create your views here.


class HomePageView(ListView):
    model = User
    template_name = 'index.html'
    context_obect_name = 'all_email_list'
'''
def showform(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form':form}

    return render(request, 'templates/index.html', context)
    '''
