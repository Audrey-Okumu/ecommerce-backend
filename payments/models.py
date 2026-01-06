from django.db import models
from orders.models import Order
# Create your models here.
#Payment Model
class Payments(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE),
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)

