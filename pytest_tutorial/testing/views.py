from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Order, Book, OrderItems, BookDomain

import json


@require_http_methods(["GET"])
def get_order_info(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        return JsonResponse(order.__dict__)
    except:
        return HttpResponse(status=404)


@login_required
@require_http_methods(["POST"])
def create_order(request):
    data = json.loads(request.body)

    order_items = data.get('order_items')

    # Create an order
    order = Order.create(user=request.user, item_count=len(order_items))
    order.save()

    # Create Order Items
    for item in order_items:
        try:
            book = Book.objects.get(pk=item.pk)

        except ObjectDoesNotExists:
            return HttpResponse({"error": f"Book with pk {item.pk}, doesn't exists."}, status=404)

        try:
            order_item = OrderItems.create(book=book,
                                           order=order)
            order_item.save()

            # Reducing available book count
            book.quantity -= 1
            book.save()
        except:
            HttpResponse(
                {"error": f"Error occured while creating an Order item (Book), with pk: {item.pk}"})

    return JsonResponse({
        "message": f"Order Successfully Created, order ID: {order.pk}."
    })


@require_http_methods(["GET"])
def get_book_info(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        return JsonResponse(book.__dict__)
    except:
        return HttpResponse(status=404)


@login_required
@require_http_methods(["POST"])
def create_book(request):
    data = json.loads(request.body)
    name = data.get("name")
    description = data.get("description")
    quantity = data.get("quantity")
    price = data.get("price")
    domain_name = data.get('domain').get('name')

    try:
        domain = BookDomain.objects.get(name=domain_name)
    except ObjectDoesNotExists:
        return HttpResponse({"error": f"Domain doesn't exists: {domain_name}"})

    try:
        book = Book.objects.create(name=name,
                                   description=description,
                                   quantity=quantity,
                                   price=price,
                                   domain=domain)
        book.save()

    except:
        return HttpResponse({"error": f"Error Creating Book {name}"})

    return JsonResponse({
        "message": f"Book Successfully created : Book ID : {book.pk}"
    })
