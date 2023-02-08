from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from stackOverFlow import settings
from stackOverFlow.manager import UserManager


class UserModel(AbstractUser):
    first_name = models.CharField(max_length=64,null= False)
    last_name = models.CharField(max_length=64, null= False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,null=False)
    username = None

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class MyPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posts',null=False)
    text = models.TextField(max_length=500, blank=True,null=True)
    location = models.CharField(max_length=30, blank=True,null=True)
    posted_on = models.DateTimeField(auto_now_add=True,null=True)
    vote = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="voters",
                                   blank=True,
                                   symmetrical=False)
    

    class Meta:
        ordering = ['-posted_on']

    def number_of_votes(self):
        if self.vote.count():
            return self.vote.count()
        else:
            return 0
        
    def voted_by(self):
        userList = []
        for p in self.vote.all():
            data = {
                "name":p.first_name,
                "email":p.email
            } 
            userList.append(data)
        return userList
    
    def __str__(self):
        return f'{self.author}\'s post'



