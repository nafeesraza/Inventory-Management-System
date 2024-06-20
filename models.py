from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_SOURCE_CHOICES = [
        ('website', 'Website'),
        ('amazon', 'Amazon'),
        ('flipkart', 'Flipkart'),
    ]

    order_id = models.CharField(max_length=255, unique=True)
    source = models.CharField(max_length=50, choices=ORDER_SOURCE_CHOICES)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class StockTransfer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    quantity = models.IntegerField()
    transfer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transfer {self.product.name} from {self.from_location} to {self.to_location}'
from django.db import models


