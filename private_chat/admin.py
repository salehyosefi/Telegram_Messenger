from django.contrib import admin
from .models import Detail

class AdminMode(admin.ModelAdmin):
    list_display = ['name', 'type', 'date']
    search_fields = ['name', 'type']

admin.site.register(Detail, AdminMode)
