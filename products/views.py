from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic.base import TemplateView
from common.views import CommonMixim
from django.core.paginator import Paginator
from products.models import Product, Category, Orders
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProductsForm


class IndexView(CommonMixim, TemplateView):
    template_name = 'products/index.html'
    title = 'Stores'


# @method_decorator(login_required, name='dispatch')
class ProductsListView(CommonMixim, ListView):
    model = Product
    template_name = 'products/store.html'
    title = 'Stores - Каталог'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category__id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = Category.objects.all()

        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Фильтруем заказы только для аутентифицированных пользователей
            context['order'] = Orders.objects.filter(user=self.request.user)
        else:
            # Для анонимных пользователей не фильтруем заказы
            context['order'] = Orders.objects.all()

        return context


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Orders.objects.filter(user=request.user, products=product)
    if not basket.exists():
        Orders.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, basket_id):
    basket = Orders.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def products_detailed(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', {'product': product})


def product_edit(request):
    product = Product.objects.all()
    context = {
        'title': 'Редактирование товара',
        'products': product
    }
    return render(request, 'products/edit.html', context=context)


def product_create(request):
    if request.method == 'POST':
        form = ProductsForm(files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:edit'))
    else:
        form = ProductsForm()

    product = Product.objects.all()
    context = {
        'title': 'Создание товара',
        'form': form,
        'products': product,
    }
    return render(request, 'products/edit.html', context=context)