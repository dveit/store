from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from products.models import ProductCategory, Product, Cart


# Create your views here.
# контроллеры = views = функция


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'Store - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)  # 3- количество продуктов на странице
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})
    return render(request, 'products/products.html', context)


@login_required
def cart_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
        return HttpResponseRedirect(current_page)


@login_required
def cart_delete(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
