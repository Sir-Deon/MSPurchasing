from django.contrib import admin
from .models import Product, Vendor, Purchase

# Register your models here.
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Purchase)
