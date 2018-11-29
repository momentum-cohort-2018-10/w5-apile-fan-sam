from django.db import models
from django.contrib.auth.models import User


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Post(Timestamp):
    title = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)


class Vote(models.Model):
    vote = models.BooleanField(null=False)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('voter', 'post')
