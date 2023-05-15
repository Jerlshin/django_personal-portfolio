from django.contrib import admin
from .models import Project
#importing the Poject class from the models.py file

admin.site.register(Project)
#inorder to see the projects in the web