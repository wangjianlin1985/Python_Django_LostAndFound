from django.contrib import admin
from apps.LostFound.models import LostFound

# Register your models here.

admin.site.register(LostFound,admin.ModelAdmin)