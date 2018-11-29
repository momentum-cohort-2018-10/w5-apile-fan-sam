from django.shortcuts import render
from posts.models import Post, Vote
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts
    })


def get_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {
        'post': post
    })


def make_vote(request, slug):
    post = Post.objects.get(slug=slug)
    user = request.user

    if request.is_ajax():
        if user.is_authenticated:

            if request.POST['vote'] == 'true':
                if user.vote_set.filter(post=post):
                    vote = user.vote_set.get(post=post)
                    if vote.vote is True:
                        vote.delete()
                    else:
                        vote.vote = True
                        vote.save()

                else:
                    vote = Vote.objects.create(vote=True,
                                               voter=request.user,
                                               post=post)
                    vote.save()

            elif request.POST['vote'] == 'false':
                if user.vote_set.filter(post=post):
                    vote = user.vote_set.get(post=post)
                    if vote.vote is True:
                        vote.vote = False
                        vote.save()
                    else:
                        vote.delete()

                else:
                    vote = Vote.objects.create(vote=False,
                                               voter=user,
                                               post=post)
                    vote.save()

        else:
            return HttpResponse(json.dumps(["fail", "You must be signed in to vote on posts."]))

        votes = post.get_total_count()
        return HttpResponse(json.dumps(["success", votes]))
