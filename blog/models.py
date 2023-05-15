from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    
    description = models.TextField()
    
    date = models.DateField()
    
    def __str__(self):
        return self.title
#this is because, in admin/ page, to veiw the actual blog name in the outline