"""user admin classes"""

from django.contrib import admin

# Register your models here.
from users.models import Profile

# admin.site.register(Profile) one way to register in admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = ('pk', 'user', 'phone_number', 'website',  'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = [
        ('Profile', {
            'fields':
                (
                    ('user', 'picture'),
                    # ('phone_number', 'website')
                ),

        }),
        ('Extra Info', {
            'fields': (
                (
                    ('website', 'phone_number'),
                    ('biography')
                )
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'))
        }
        )
    ]


    readonly_fields = ('created', 'modified')


class ProfileInline (admin.StackedInline):
    """profile inline  admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

