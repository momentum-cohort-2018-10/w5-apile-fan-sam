from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import json
from posts.models import Post, User
from django.template.defaultfilters import slugify


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'post_data', file)


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Post.objects.all().delete()
        user = User.objects.get(username="fan")

        with open(get_path('posts.json'), 'r') as file:
            reader = json.load(file)

            i = 0

            for post in reader:

                post = Post(
                    title=reader[i]['title'],
                    slug=slugify(reader[i]['title']),
                    author=user
                )
                if reader[i]['link']:
                    post.link = reader[i]['link']

                if reader[i]['description']:
                    post.description = reader[i]['description']

                post.save()
                i += 1
