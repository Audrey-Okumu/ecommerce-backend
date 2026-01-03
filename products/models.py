from django.db import models
from django.conf import settings
# Create your models here.

#Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
#Product Model

class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')  # allows accessing all products of a category via category.products.all()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock_qty=models.PositiveIntegerField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return self.name
    

