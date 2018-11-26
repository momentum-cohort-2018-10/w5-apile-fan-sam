from django.contrib import admin
from posts.models import Post
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'link', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.unregister(User)
admin.site.register(User)
