from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dog_age = models.IntegerField()
    dog_weight = models.IntegerField()
    dog_gender = models.CharField(max_length=7)
    dog_breed = models.CharField(max_length=50)
    # additional
    dog_pictures = models.URLField(blank=True)

    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
