from django.contrib import admin

from .models import CustomUser, Teams

# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    list_display = ('id', 'FullName')

admin.site.register(CustomUser)
admin.site.register(Teams, TeamsAdmin)