from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def home(request):
  return HttpResponse("Welcome django")
  
def register(request):
  if request.method=='POST':
    form=RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      
  else:
      form=RegisterForm()
  return render(request,'register.html',{'form':form})

  #new branch