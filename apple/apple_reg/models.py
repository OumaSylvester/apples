from django.db import models

# Create your models here.
class Apple(models.Model):
    id = models.AutoField(primary_key=True)
    year_of_production = models.IntegerField()
    breed = models.CharField(max_length=100)
    raw = models.BooleanField()
    column = models.CharField(max_length=100)
    geolocation = models.CharField(max_length=100)

    def __str__(self):
        return self.id