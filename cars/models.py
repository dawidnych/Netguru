from django.db import models


class Cars(models.Model):
    make = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)


class Rate(models.Model):
    rating = models.IntegerField(blank=False)
    car_id = models.ForeignKey(Cars, related_name="cars", on_delete=models.CASCADE)
