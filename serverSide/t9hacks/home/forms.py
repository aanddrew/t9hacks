import datetime

from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class meta:
        email = User
        fields=['name', 'email', 'score']

