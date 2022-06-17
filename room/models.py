from django.db import models
from django.contrib.auth import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=55)


class Room(models.Model):
    name = models.CharField(max_length=50)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.textField(max_length = 250)
    # created_at = 
    # updated_at = 


class Message(models.Model):
    room_id = models.ForeignKey(Room, on_delete = models.CASCADE)
    sender = models.ForeignKey(User,on_delete = models.CASCADE)
    text = models.textField(max_length = 250)
