from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='media/profile_imgs', default='media/profile_imgs/blank.png')
    
    def __str__(self):
        return self.user.username


class Room(models.Model):
    name=models.CharField(max_length=30)
    room_id=models.AutoField(primary_key=True)
    open=models.CharField(max_length=10, default="yes")
    #yes no
    def __str__(self):
        return self.name
    
class Permission(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, default="normal")
    #normal owner admin ban mute
    
    
    
    def __str__(self):
        return self.user.user.username +  self.room.name  
    

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='recipient')
    message = models.CharField(max_length=3000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    message_id=models.AutoField(primary_key=True)
    #is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
    
   