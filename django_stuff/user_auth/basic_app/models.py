from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # Extend the user class to add more details (profile picture, bio, ... )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)  # profile pictures saved in media/profile_pics

    def __str__(self):
        return self.user.username  # default attribute of User model