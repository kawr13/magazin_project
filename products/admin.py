from django.contrib import admin
from .models import Product, Category, Orders
# Register your models here.


admin.site.register(Orders)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'creat_at')
    readonly_fields = ('creat_at',)
    list_filter = ('category', 'creat_at', 'price')
    search_fields = ('name', 'category')
    fields = ('name', ('price', 'quantity'), 'category', 'creat_at', 'description', 'image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
