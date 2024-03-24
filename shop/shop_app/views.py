from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def index_view(request):
    context = {
        'title': "Hello world"
    }
    return render(request, "shop_app/index.html", context)


def product_list_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop_app/list.html', context)


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'shop_app/detail.html', {'product': product})












