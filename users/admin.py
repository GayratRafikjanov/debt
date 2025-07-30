from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('id', 'email')
    read_only_fields = ('id',)
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)
