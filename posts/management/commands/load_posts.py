from django.core.management.base import BaseCommand

from posts.models import Post, User, Vote
from django.template.defaultfilters import slugify
from mimesis import Person
from mimesis import Text
from random import randint, choice


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        users = User.objects.all()
        for user in users:
            if not user.is_staff:
                user.delete()

        Post.objects.all().delete()
        person = Person('en')
        text = Text('en')
        users = []
        for i in range(5):
            user = User.objects.create_user(username=person.username(),
                                            password="greenfox23")
            users.append(user)

        posts = []
        for _ in range(40):

            post = Post(
                title=text.title(),
                description=text.text(8),
                link="https://github.com/momentum-cohort-2018-10/w5-apile-fan-sam",
                author=choice(users)
            )

            post.slug = slugify(post.title) + f'-{randint(1, 255)}'
            post.save()
            posts.append(post)

        for x in range(20):
            Vote.objects.create(vote=True,
                                voter=users[0],
                                post=posts[x])

            Vote.objects.create(vote=choice((True, False)),
                                voter=users[1],
                                post=posts[x])

            Vote.objects.create(vote=True,
                                voter=users[2],
                                post=posts[x])

            Vote.objects.create(vote=choice((True, False)),
                                voter=users[3],
                                post=posts[x])

            Vote.objects.create(vote=choice((True, False)),
                                voter=users[4],
                                post=posts[x])
