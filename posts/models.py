from django.db import models
from django.contrib.auth.models import User


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamp):
    title = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.title

    def get_total_count(self):
        upvotes = Vote.objects.filter(vote=True, post=self).count()
        downvotes = Vote.objects.filter(vote=False, post=self).count()
        return upvotes - downvotes


class Vote(models.Model):
    vote = models.BooleanField(null=False)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('voter', 'post')


class Comment(Timestamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
