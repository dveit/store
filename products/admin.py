from django.contrib import admin

from products.models import ProductCategory, Product, Cart

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Cart)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    search_fields = ('name',)


class CartAdminInline(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp',)
    extra = 0

