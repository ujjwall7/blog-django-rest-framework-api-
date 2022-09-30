from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User




class Blog(models.Model):   
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    Title = models.CharField(max_length=250)
    Description= models.TextField()
    Image = models.ImageField(upload_to="media",null=True)
    Pub_date = models.DateTimeField('date published', auto_now_add=True)
    Author= models.CharField(max_length=50)

    def __str__(self):
        return self.Title


