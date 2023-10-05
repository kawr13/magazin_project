from django.contrib import admin
from .models import Product, Category, Orders
from django.utils.html import mark_safe
# Register your models here.


@admin.action(description='Обнуление количества')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class OrdersAdmin(admin.TabularInline):
    model = Orders
    fields = ('products', 'quantity', 'create_at')
    readonly_fields = ('create_at',)
    extra = 0


@admin.action(description='Выставить')
def set_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def set_not_published(modeladmin, request, queryset):
    queryset.update(is_published=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'creat_at', 'quantity', 'is_published', 'display_image')
    readonly_fields = ('creat_at',)
    list_filter = ('category', 'creat_at', 'price')
    search_fields = ('name', 'category')
    fields = ('name', ('price', 'quantity'), 'category', 'creat_at', 'description', 'image')
    actions = [reset_quantity, set_published, set_not_published]

    def display_image(self, obj):
        # Здесь вы можете создать HTML-код для отображения изображения
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="50" height="50" />')
        else:
            return 'Нет изображения'
        
    display_image.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
