from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'phone', 'image_tag']


admin.site.register(Profile, ProfileAdmin)
