"""Platzigram URLs module."""

from django.urls import path
from django.conf.urls.static import static
from platzigram import views as local_views
from posts import views as posts_views
from django.conf import settings
from users import views as users_views


from django.contrib import admin

urlpatterns = [
    path('hello-world/', local_views.hello_world, name = 'hello_wordld'),
    path('sorted/', local_views.sort_integers, name='sorted'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='say_hi'),
    path('posts/', posts_views.list_views, name='feed' ),
    path('admin/',admin.site.urls, name='admin'),
    path('users/login/',users_views.login_view, name='login'),
    path('users/logout/',users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
