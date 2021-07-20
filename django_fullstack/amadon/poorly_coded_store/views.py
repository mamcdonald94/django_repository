from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if 'total_quantity' not in request.session:
        request.session['total_quantity'] = 0
    if 'total_price' not in request.session:
        request.session['total_price'] = 0

    if "product.id" in request.POST:
        product_purchased = Product.objects.get(id='product.id')
        request.session['price_from_form'] = float(product_purchased.price)
        print(product_purchased.price)
    request.session['quantity_from_form'] = int(request.POST["quantity"])
    
    request.session['total_charge'] = request.session['quantity_from_form']  * request.session['price_from_form']
    print("Charging credit card...")
    request.session['total_quantity'] += request.session['quantity_from_form'] 
    request.session['total_price'] += request.session['price_from_form']

    return redirect('success/')

def checkout_success(request):
    context = {
        "order": Order.objects.create(quantity_ordered=request.session['quantity_from_form'], total_price=request.session['price_from_form']),
    }
    return render(request, "store/checkout.html", context)