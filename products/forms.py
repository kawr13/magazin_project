from django import forms
from .models import Product, Category





class ProductsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование'}), label='Наименование', error_messages={
            'required': 'Это поле обязательно для заполнения.'  # Ваше сообщение об ошибке здесь
        },)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Цена', error_messages={
            'required': 'Это поле обязательно для заполнения.'  # Ваше сообщение об ошибке здесь
        },)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Описание', error_messages={
            'required': 'Это поле обязательно для заполнения.'  # Ваше сообщение об ошибке здесь
        },)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Выберите категорию',
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Это поле обязательно для заполнения.'  # Ваше сообщение об ошибке здесь
        },
        label='Категория',
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-group',
    }), label='Изображение',
        error_messages={
            'required': 'Выберите изображение'  # Ваше сообщение об ошибке здесь
        },
    )
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Количество', error_messages={
            'required': 'Это поле обязательно для заполнения.'  # Ваше сообщение об ошибке здесь
        },)


    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'image', 'quantity')