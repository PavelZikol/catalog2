from django.shortcuts import render

from catalog.models import Product
# Create your views here.
def products(request):
    context = {
        'object_list' : Product.objects.all(),
        'title': 'Продукты'
    }
    return render(request, 'catalog/product_list.html', context=context)

def description(request,pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list' : Product.objects.filter( pk=pk),
        'title': 'Продукты'
    }
    return render(request, 'catalog/description.html', context=context)