from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# why we using blank in django
# we can create a profile for users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True , null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/' , blank=True , null=True)
    email = models.EmailField(blank=True , null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'