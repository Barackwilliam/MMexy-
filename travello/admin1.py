from django.contrib import admin
from .models import Category, Package, PackageImage

class PackageImageInline(admin.TabularInline):
    model = PackageImage
    extra = 1

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'package_level', 'price_type', 'price']
    list_filter = ['category', 'package_level', 'price_type']
    search_fields = ['name', 'description']
    inlines = [PackageImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

admin.site.register(PackageImage)