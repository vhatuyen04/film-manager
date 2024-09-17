from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django import forms
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length = 255)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    youtube_url = models.URLField(blank=True, null=True)
    film_file = models.FileField(upload_to='films/', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='films')
    def __str__(self):
        return self.title
    def is_youtube(self):
        return bool(self.youtube_url)
    def is_local(self):
        return bool(self.film_file)
    
class Admin(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    USERNAME_FIELD = 'username'

    # def __str__(self):
    #     return self.username

    def check_password(self, raw_password):
        """
        Check if the raw password matches the hashed password stored in the database.
        """
        return raw_password == self.password  # Implement your password comparison logic

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Admin
        fields = ['username', 'password']  