from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from app.users.models import UserConfiguration


@admin.register(UserConfiguration)
class UserConfigurationAdmin(ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'user']
    search_fields = ['user__email']


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ['email', 'username', ]


admin.site.site_title = "Admin Panel"
admin.site.site_header = "Admin Panel"
admin.site.index_title = "Administration"
