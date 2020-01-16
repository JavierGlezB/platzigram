"""Platzigram URLs module."""

from django.urls import path
from django.conf.urls.static import static
from platzigram import views as local_views
from posts import views as posts_views
from django.conf import settings

from django.contrib import admin

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/', posts_views.list_views),
    path('admin/',admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
