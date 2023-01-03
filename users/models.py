from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=300)
    bio = models.CharField(max_length=1000)
    age = models.CharField(max_length=5)
    experience_years = models.CharField(max_length=5)
    projects = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    workplace = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 350:
            output_size = (400, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)
