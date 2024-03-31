from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='cars', blank=True, null=True)
    photo_url = models.URLField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

