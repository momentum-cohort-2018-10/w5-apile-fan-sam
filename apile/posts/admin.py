from django.contrib import admin
from posts.models import Post, User
from django.contrib.auth.admin import UserAdmin


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'link', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
