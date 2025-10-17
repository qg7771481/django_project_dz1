from django.contrib import admin

from .models import Product, Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Налаштування відображення моделі Category в адмін-панелі."""
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['created', 'available']
    list_editable = ['price', 'available']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'country']
    list_editable = ['country']
