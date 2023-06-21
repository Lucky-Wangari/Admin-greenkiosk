from django.contrib import admin

# Register your models here.
from .models import Vendor
class VendorAdmin(admin.ModelAdmin):
    list_display = ()
    
admin.site.register(Vendor,VendorAdmin)