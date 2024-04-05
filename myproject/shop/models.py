from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100,null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
