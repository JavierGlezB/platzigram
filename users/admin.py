"""user admin classes"""

from django.contrib import admin

# Register your models here.
from users.models import Profile



#admin.site.register(Profile) one way to register in admin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = ( 'pk','user', 'phone_number','website',  'picture')  
    list_display_links = ( 'pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')


 