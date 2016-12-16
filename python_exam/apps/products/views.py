from django.shortcuts import render, redirect
from .models import Product
from ..regandlogin.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    context ={
        'products': Product.objects.all(),
    }
    return render(request, 'products/index.html', context)

def createpage(request):
    return render(request, 'products/create.html')

def create(request):
    if request.method == 'POST':
        errors = Product.objects.validate_product(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('products:products_createpage')
        else:
            userobj = User.objects.get(id = request.session['user'])
            new_product = Product.objects.create(name = request.POST['product'], user = userobj)
            new_product.save()
            print new_product.user.name
    return redirect('products:products_index')

def delete(request, id):
    if request.method== 'GET':
        product_delete = Product.objects.get(id=id)
        product_delete.delete()
        return redirect('products:products_index')

def wishpage(request, id):
    context = {
        'items': Product.objects.filter(id = id)
    }
    return render(request, 'products/wishitems.html', context)

def wishadd(request, id):
    Product.objects.filter(id=id)
    user = User.objects.get(id=request.session['user'])
    product = Product.objects.get(id=id)
    user.wish.add(product)
    user.save()
    print User.wish.id
    return redirect('products:products:index')
