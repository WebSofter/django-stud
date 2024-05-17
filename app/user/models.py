from django.db import models
from django. contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, null=True, blank=True, choices=[('m', 'f')])
    birth_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True, default=True)

    def _str_(self):
        return self.user.username
    
@receiver (post_save, sender=User)
def create_user_profile (sender, instance, created, **kwargs):
    print(sender)
    if created:
        Profile.objects.create(user=instance)