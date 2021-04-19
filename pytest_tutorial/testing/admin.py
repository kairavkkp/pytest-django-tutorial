from django.contrib import admin
from .models import OrderItems, Order, BookDomain, Book
# Register your models here.

admin.register(Order)
admin.register(OrderItems)
admin.register(BookDomain)
admin.register(Book)
