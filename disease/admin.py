from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = User

admin.site.register(models.City)
admin.site.register(models.Symptoms)
admin.site.register(models.User, UserAdmin)
