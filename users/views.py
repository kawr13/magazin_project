from django.shortcuts import render, HttpResponseRedirect
from .models import Users
from products.models import Orders
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from  django.urls import reverse
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=user, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)



def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    context = {
        'title': 'Профиль',
        'orders': Orders.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            message = 'Вы успешно зарегистрировались'
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'users/registr.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


