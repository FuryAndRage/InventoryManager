from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from InventoryManager.category.models import Category




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
                product_image = form.cleaned_data['product_image']
            )
            data_from_form.save()
            # Insert success Message here
            return redirect('product:list')
    return render(request, 'productAddModal.html', {'form':form,})

    # if request.method != 'POST':
    #     return render(request, '')
