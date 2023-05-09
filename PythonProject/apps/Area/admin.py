from django.contrib import admin
from apps.Area.models import Area

# Register your models here.

admin.site.register(Area,admin.ModelAdmin)