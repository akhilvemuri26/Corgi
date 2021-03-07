from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional

    dog_breed = models.CharField(max_length=50, blank=True)

    profile_pictures = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class HealthInfo(models.Model):
    symptom1 = models.CharField(max_length=50, blank=True)
    symptom2 = models.CharField(max_length=50, blank=True)
    symptom3 = models.CharField(max_length=50, blank=True)
