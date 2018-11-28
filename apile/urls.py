from django.contrib import admin
from django.urls import path, include
from posts import views
from posts.backends import HomeRegistrationView

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/<slug>', views.get_post, name="get_post"),
    path('accounts/register/',
         HomeRegistrationView.as_view(),
         name="registration_register"),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]
