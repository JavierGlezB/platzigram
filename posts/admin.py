from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'photo',
        'created',
        'modified')
    list_filter = (
        'title',
        'photo',
        'created',
        'modified')
