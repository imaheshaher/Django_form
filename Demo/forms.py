from django.forms import ModelForm
from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
  class Meta:  
    model=Register
    fields=['first_name','last_name','address']