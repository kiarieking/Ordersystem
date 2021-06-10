from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


# Create your views here.
def home(request):
    chicken = get_object_or_404(Category, pk=1)
    dairy = get_object_or_404(Category, pk=2)
    pig = get_object_or_404(Category, pk=3)
    context = {'chicken': chicken, 'dairy': dairy, 'pig': pig}
    return render(request, 'product/home.html', context)


def product_display(request):
    chicken_feeds = Product.objects.filter(category__categoryname__contains="Poultry feeds")
    dairy_feeds = Product.objects.filter(category__categoryname__contains="Dairy Farm feeds")
    pig_feeds = Product.objects.filter(category__categoryname__contains="Pig Farm feeds")
    chicken = get_object_or_404(Category, pk=1)
    dairy = get_object_or_404(Category, pk=2)
    pig = get_object_or_404(Category, pk=3)
    context = {'chicken_feeds': chicken_feeds, 'dairy_feeds': dairy_feeds, 'pig_feeds': pig_feeds
               ,'chicken': chicken, 'dairy': dairy, 'pig': pig}
    return render(request, 'product/products.html', context)


def add_product(request):
    p_name = request.POST.get('productname')
    p_cost = request.POST.get('productcost')
    p_quantity = request.POST.get('productquantity')
    p_image = request.FILES.get('productimage')
    p = Product(productname=p_name, productcost=p_cost, productquantity=p_quantity, productimage=p_image)
    p.save()
    return redirect(product_display)


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


def place_order(request):
    return render(request, 'product/poultry_order.html')


def dairy_order(request):
    return render(request, 'product/dairy_order.html')


def total_order(request):

    return render(request, '')