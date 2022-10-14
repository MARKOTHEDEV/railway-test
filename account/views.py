from django.shortcuts import render
from . import models,form
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.method =='POST':
        instance = form.InfoForm(request.POST)
        if instance.is_valid():
            instance.save()
            
    return render(request,'index.html',{'all_info':models.Info.objects.all()})
