from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from .models import *

from .forms import UserForm

from .apistuff import *


# Create your views here.


class HomePageView(ListView):
    model = User
    template_name = 'index.html'
    context_obect_name = 'all_email_list'

def add_User_Form_Submission(request):
    print("yooooooo")
    _name = request.POST["name"]
    _email = request.POST["email"]
    _kills = 0
    _tokens = 0
    NewUser = User(name = _name, email = _email, kills = _kills, tokens = _tokens)

    NewUser.save()

    return render(request, 'index.html')


