from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


# Create your views here.
def home(request):
    return render(request, 'product/home.html')


def get_carousel_images(request, id):
    carousel_img = get_object_or_404(Category, pk=id)
    context = {"carousel_img": carousel_img}
    return render(request, 'product/home.html', context)


def product_display(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'product/products.html', {'products': products})


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
