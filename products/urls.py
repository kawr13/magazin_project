"""
URL configuration for magazin_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import ProductsListView, basket_add, basket_remove, products_detailed, product_edit, product_create


app_name = 'products'


urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('categories/<int:category_id>/', ProductsListView.as_view(), name='categories'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('detailed/<int:product_id>/', products_detailed, name='detailed'),
    path('edit/', product_edit, name='edit'),
    path('create/', product_create, name='create'),
]


