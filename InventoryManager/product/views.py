from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from .models import Product
from .forms import ProductForm
from InventoryManager.category.models import Category
from django.http import Http404



def product_list(request):
    category = Category.objects.filter(user = request.user.id)
    products = Product.objects.filter(user = request.user.id)
    return render(request, 'product_list.html', {'products':products, 'category':category})

def product_add(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data_from_form = Product(
                user = form.cleaned_data['user'],
                category = form.cleaned_data['category'],
                product_name = form.cleaned_data['product_name'],
                product_description = form.cleaned_data['product_description'],
                product_quantity = form.cleaned_data['product_quantity'],
                product_image = form.cleaned_data['product_image'],
              
            )
            data_from_form.save()
            # Insert success Message here
            return redirect('product:list')
    return render(request, 'productAddModal.html', {'form':form,})

def product_detail(request, pk):
    category = Category.objects.filter(user = request.user.id)
    product = get_object_or_404(Product, pk = pk)
    return render(request, 'product_detail.html', {'product':product, 'category':category})


def product_search(request):
    category = Category.objects.filter(user = request.user.id)
    products = Product.objects.filter(user = request.user.id)
    if request.method == 'GET':
        search = request.GET.get('search')
        products = products.filter(product_name__icontains = search)
    return render(request, 'product_list.html', {'products':products, 'category':category})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk = pk)
    if product.user != request.user:
        raise Http404
    # form = ProductForm(request.POST or None, request.FILES or None, instance = product)
    if request.method == 'POST':
        product.delete()
        return redirect('product:list')
    return render(request, 'productDeleteModal.html', {'product':product})
