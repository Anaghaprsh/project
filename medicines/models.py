# medicines/models.py

from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    components = models.TextField()
    low_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class AlternateMedicine(models.Model):
    original_medicine = models.ForeignKey(Medicine, related_name='alternatives', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    components = models.TextField()
    low_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
