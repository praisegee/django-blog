from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    name= models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.EmailField(unique = True)
    bio = models.TextField(max_length= 500)
    img = models.ImageField(blank= True, null= True)
    date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(name=instance)

