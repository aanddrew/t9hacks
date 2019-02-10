from django.db import models

from django.forms import ModelForm

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, blank=True)
    kills = models.IntegerField()
    tokens = models.IntegerField()
    
    def __str__(self):
        return self.name

'''
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'score']
        '''
