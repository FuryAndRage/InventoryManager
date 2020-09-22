from django.shortcuts import render, get_object_or_404, redirect
from InventoryManager.product.models import Product
from .models import WithdrawalProduct
from .forms import WithdrawalForm

def withdrawal_product(request, pk):
    product = get_object_or_404(Product, pk = pk)
    form = WithdrawalForm()
    if request.method == 'POST':
        form = WithdrawalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data_from_form = WithdrawalProduct(
                user = form.cleaned_data['user'],
                product = form.cleaned_data['product'],
                withdrawal_time = form.cleaned_data['withdrawal_time'],
                withdrawal_quantity = form.cleaned_data['withdrawal_quantity'],
                withdrawal_reason = form.cleaned_data['withdrawal_reason']
            )
            data_from_form.save()
            return redirect('product:list')
    
    return render(request, 'withdrawalProductModal.html', {'form':form, 'product':product})
