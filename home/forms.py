import datetime

from django.forms import ModelForm
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS

class UserForm(ModelForm):
    class meta:
        email = User
        fields=['name', 'email', 'score']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
