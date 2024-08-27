from django.contrib import admin
from .models import Category, Brand, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')  # Updated 'photo' to 'image'

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')  # Updated 'photo' to 'image'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'brand', 'price', 'description')
