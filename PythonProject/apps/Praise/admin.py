from django.contrib import admin
from apps.Praise.models import Praise

# Register your models here.

admin.site.register(Praise,admin.ModelAdmin)