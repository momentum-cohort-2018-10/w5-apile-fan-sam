from django.contrib import admin
from django.urls import path, include
from posts import views
from posts.backends import HomeRegistrationView

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/new', views.make_post, name="make_post"),
    path('posts/<slug>', views.get_post, name="get_post"),
    path('posts/<slug>/delete', views.delete_post, name="delete_post"),
    path('my-posts/', views.get_user_posts, name="get_user_posts"),
    path('posts/<slug>/vote', views.make_vote, name="make_vote"),
    path('comments/<id>/delete', views.delete_comment, name="delete_comment"),
    path('accounts/register/',
         HomeRegistrationView.as_view(),
         name="registration_register"),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]
