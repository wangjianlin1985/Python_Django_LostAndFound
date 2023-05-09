from django.contrib import admin
from apps.LookingFor.models import LookingFor

# Register your models here.

admin.site.register(LookingFor,admin.ModelAdmin)