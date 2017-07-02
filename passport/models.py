from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#User先用大写试试
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(max_length=51200)
    scope = models.IntegerField(default=100)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
