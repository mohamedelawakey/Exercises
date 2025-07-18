from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description =  models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
