from django.contrib import admin
from posts.models import Post, Vote, Comment
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'link', 'description')
    prepopulated_fields = {'slug': ('title',)}


class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ('vote', 'voter', 'post')


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('text', 'post', 'commenter')


admin.site.register(Post, PostAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Comment, CommentAdmin)
