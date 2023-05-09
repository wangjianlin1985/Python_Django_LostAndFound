from django.contrib import admin
from apps.Claim.models import Claim

# Register your models here.

admin.site.register(Claim,admin.ModelAdmin)