from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from .models import *

from .forms import UserForm

# Create your views here.


class HomePageView(ListView):
    model = User
    template_name = 'index.html'
    context_obect_name = 'all_email_list'

def add_User_Form_Submission(request):
    print("yooooooo")
    _name = request.POST["name"]
    _email = request.POST["email"]

    NewUser = User(name = _name, email = _email, score = 0)

    NewUser.save()

    return render(request, 'index.html')




'''
def showform(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form':form}

    return render(request, 'templates/index.html', context)
    '''
