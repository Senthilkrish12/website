from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)  # You can host images somewhere or upload later
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
