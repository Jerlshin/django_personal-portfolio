from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    #shifting the database to web,
    return render(request, 'portfolio/home.html', {'projects':projects})
#all the Porject class codes from the models.py is imported and sent to portfolio/home.html 
#and with disctionary 'projects' : with passowrd 'projects'
  