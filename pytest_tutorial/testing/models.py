from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BookDomain(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    domain = models.ForeignKey('BookDomain', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_count = models.IntegerField()

    def increment_item_count(self):
        self.item_count += 1
        self.save()


class OrderItems(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
