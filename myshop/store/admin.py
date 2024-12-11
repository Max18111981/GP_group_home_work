from django.contrib import admin
from .models import Product, Category, Order, CartItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'category')
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CartItemInline(admin.TabularInline):
    model = CartItem
    fields = ('product', 'quantity', 'total_price')
    readonly_fields = ('total_price',)
    extra = 0

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'  # Наз


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'order_date', 'created_at')
    list_filter = ('order_date',)
    search_fields = ('customer_name', 'customer_email')
    inlines = [CartItemInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
