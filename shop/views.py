from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import time

from payment.views import razorpay_client
from .forms import *
# Create your views here.
from .models import *


def shop_grid_view(request):
    items = ItemsForSale.objects.all()
    count = ItemsForSale.objects.count()
    offer_items = ItemsForSale.objects.filter(offer=True)
    return render(request, 'shop-grid.html',
                  {'items': items, 'offer_items': offer_items, 'count': count})


def shop_details_view(request, id):
    try:
        obj = get_object_or_404(ItemsForSale, id=id)
        context = {'obj': obj}
        return render(request, 'shop-details.html', context)
    except ItemsForSale.DoesNotExist:
        raise Http404("ItemForSale does not exist")


@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(ItemsForSale, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.create(cart=cart, item=item)

    if request.method == 'POST':
        if cart_item:
            return redirect('/shopping-cart')
    else:
        return redirect('/shop-details' + '/' + str(item_id))


@login_required
def shopping_cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    cart_items = cart.cartitem_set.all() if cart else []

    total_price = sum(item.item.price for item in cart_items) if cart_items else 0

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'item_count': len(cart_items),
        'total_price': total_price,
    }
    return render(request, 'shopping-cart.html', context)


def department_view(request, cat):

    obj = ItemsForSale.objects.filter(category=cat)

    count = len(obj)

    context = {'obj': obj, 'cat': cat, 'count': count}

    # Render the template with the given context
    return render(request, 'category.html', context)


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    messages.success(request, 'Item removed from cart successfully.')
    return redirect('/shopping-cart')


from django.db import transaction

@login_required(redirect_field_name="/login/")
def checkout_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    cart_items = cart.cartitem_set.all() if cart else []
    total_price = sum(item.item.price for item in cart_items) if cart_items else 0
    context = {}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # Create an order
                order = Order(
                    user=request.user,
                    name=form.cleaned_data['name'],
                    address=form.cleaned_data['address'],
                    city=form.cleaned_data['city'],
                    postcode=form.cleaned_data['postcode'],
                    phone=form.cleaned_data['phone'],
                    notes=form.cleaned_data['notes'],
                    total_price=total_price
                )
                order.price = total_price * 100
                currency = 'INR'
                razorpay_order = razorpay_client.order.create(dict(amount=float(order.price),
                                                                   currency=currency,
                                                                   payment_capture='0'))
                razorpay_order_id = razorpay_order['id']
                order.razorpay_order_id = razorpay_order_id
                order.save()

                # Decrease stock for each item in the cart
                for cart_item in cart_items:
                    item = cart_item.item
                    item.stock -= 1  # Decrease stock by one
                    item.save()

                # Clear the cart
                Cart.objects.filter(user=request.user).delete()

                callback_url = ' http://127.0.0.1:8000/payment/success'
                context = {'razorpay_order_id': razorpay_order_id, 'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
                           'razorpay_amount': order.price, 'currency': currency, 'callback_url': callback_url,
                           "order": order}
                # You can perform any additional logic here, such as creating invoices, processing payments, etc.
                # Redirect to a success page or do other necessary actions.
    else:
        form = OrderForm()

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'form': form
        }

    return render(request, 'checkout.html', context)
