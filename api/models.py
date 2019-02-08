from django.db import models


class Car(models.Model):
    """
    All: ['price', 'year_model', 'mileage', 'fuel_type', 'mark',
    'model', 'fiscal_power', 'sector', 'type', 'city']
    Less: ['price', 'year_model', 'mileage',
    'fiscal_power', 'fuel_type', 'mark']
    """
    price = models.PositiveIntegerField(blank=True)  # label to predict

    year_model = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    fiscal_power = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20)
    mark = models.CharField(max_length=30)
