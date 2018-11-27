from django.contrib import admin
from posts.models import Post, Vote
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'link', 'description')
    prepopulated_fields = {'slug': ('title',)}


class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ('vote', 'voter', 'post')


admin.site.register(Post, PostAdmin)
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Vote, VoteAdmin)
