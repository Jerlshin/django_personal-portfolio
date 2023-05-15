from django.db import models

class Project(models.Model):
#take the reference form the Django 'model Feild type' from the online source
    title = models.CharField(max_length = 100)
    
    description = models.CharField(max_length = 250)
    
    image = models.ImageField(upload_to='portfolio/images/', blank = True)
    
    url = models.URLField(blank=True)
    
    #the blank=True will allow the feild to be left blank
    #Flase, if it is left blank, it would raise an error

    def __str__(self):
        return self.title

#for making the project name dislayed in the admin/ 
    
    