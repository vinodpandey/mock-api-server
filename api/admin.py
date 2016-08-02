from .models import Api
from django.contrib import admin


class ApiAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'status', 'response', 'is_enabled')
admin.site.register(Api, ApiAdmin)
