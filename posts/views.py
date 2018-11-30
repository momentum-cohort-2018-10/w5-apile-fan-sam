from django.shortcuts import render, redirect
from posts.models import Post, Vote
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.forms import PostForm
from django.utils.text import slugify
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


@login_required
def make_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(**form.cleaned_data)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()

            return redirect('home')

    return render(request, 'posts/post_form.html', {
        'form': form
    })


@login_required
def get_user_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    return render(request, 'posts/user_posts.html', {
        'posts': posts
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
