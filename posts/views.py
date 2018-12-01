from django.shortcuts import render, redirect
from posts.models import Post, Vote, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.forms import PostForm, CommentForm
from django.utils.text import slugify
from django.db.models import Count
import json


def index(request):
    posts = Post.objects.annotate(num_comments=Count('comment'))
    return render(request, 'index.html', {
        'posts': posts
    })


def get_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(**form.cleaned_data)
            comment.commenter = request.user
            comment.post = post
            comment.save()
            messages.add_message(request,
                                 messages.INFO,
                                 'Your comment was published.')

    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    return render(request, 'posts/post.html', {
        'form': form,
        'comments': comments,
        'post': post
    })


@login_required
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if (request.user == post.author) or (request.user.is_staff):
        post.delete()
    return redirect('home')


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
            messages.add_message(request,
                                 messages.INFO,
                                 'Your post was published.')
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


@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    post = comment.post
    comment.delete()
    messages.add_message(request,
                         messages.INFO,
                         'Your comment was deleted.')
    return redirect('get_post', slug=post.slug)


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
            return HttpResponse(
                json.dumps(["fail",
                            "You must be signed in to vote on posts."]))

        votes = post.get_total_count()
        return HttpResponse(json.dumps(["success", votes]))
