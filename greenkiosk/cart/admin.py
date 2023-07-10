from django.contrib import admin

# Register your models here.
from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ("name","total_products","number_of_products","payment_options")

admin.site.register(Cart, CartAdmin)
