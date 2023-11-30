from django.db import models

class RegisteredUser(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
