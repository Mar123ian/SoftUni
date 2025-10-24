from django.db import models

# Create your models here.


class OrderBase(models.Model):

    class Meta:
        abstract = True

    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled"),
    ]

    product_name = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    amount = models.PositiveIntegerField(default=1)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    warranty = models.CharField(max_length=255, default="No warranty")
    delivery = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product_name} for {self.customer_name}"

class Order(OrderBase):
    pass

class DeletedOrder(OrderBase):
    pass

