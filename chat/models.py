from django.db import models

class Message(models.Model):

    content = models.CharField(max_length=50, null=False)
    timestemp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
    

class Comment(models.Model):

    content = models.CharField(max_length=50, null=False)
    timestemp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
# Create your models here.
