from django.db import models
from users.models import Users
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    creat_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'Продукт: {self.name}, категория: {self.category}, цена: {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=125, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(selfs):
        return sum(basket.quantity for basket in selfs)


class Orders(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Заказ: {self.id}, пользователь: {self.user}, товары: {self.products}, количество: {self.quantity}'

    def sum(self):
        return self.quantity * self.products.price









