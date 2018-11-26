from django.db import models
from django.contrib.auth.models import AbstractUser


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    USERNAME_FIELD = 'username'


class Post(Timestamp):
    title = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
