from django.db import models

# Create your models here.
class ProductList(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_id = models.DateTimeField(auto_now=True)