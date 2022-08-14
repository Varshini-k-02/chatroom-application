from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    #Since User is already defined in another Foreign key relation 
    participants = models.ManyToManyField(User, related_name='Participants', blank=True)
    #Time stamp taken every time the post is saved - auto_now = True
    updated = models.DateTimeField(auto_now=True) 
    #Time stamp taken only once that is during the creation of the post - auto_now_add
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-updated','-created']
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # When the parent(room) is deleted, children get deleted
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-updated','-created']
        
    def __str__(self):
        return self.body[0:50]