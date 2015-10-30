from django.forms import ModelForm
#from django.forms.models import modelform_factory
from django.contrib.auth.models import User
#from GetThingsDone.models import UserDetails, toDo
from django.forms.extras.widgets import SelectDateWidget
from django import forms

class UserForm(ModelForm):
    class Meta:
        model= User
        fields=('username','first_name','last_name','password','email')
        widgets={'password':forms.PasswordInput()}


