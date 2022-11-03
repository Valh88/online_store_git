from django.contrib import admin
from .models import Catalog, SubCatalog, Product, PhotoProduct, PhotoCatalog


class PhotoProductInline(admin.TabularInline):
    model = PhotoProduct
    extra = 0


class PhotoCatalogInline(admin.TabularInline):
    model = PhotoCatalog
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoProductInline]
    list_display = ['name', 'price', 'limited_edition', 'description', 'catalog', 'created', 'updated', 'images']
    search_fields = ['name']


class ProductInLine(admin.TabularInline):
    model = Product


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'select_group', 'is_active']
    inlines = [PhotoCatalogInline, ]
    # inlines = [PhotoCatalogInline, ProductInLine]


class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'catalog', 'is_active']


class PhotoCatalogAdmin(admin.ModelAdmin):
    list_display = ['photo', 'catalog']


class PhotoProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_tag']


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(SubCatalog, SubCatalogAdmin)
# admin.site.register(PhotoCatalog, PhotoCatalogAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PhotoProduct, PhotoProductAdmin)
