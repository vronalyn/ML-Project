from django.db import models

# Create your models here.

class WaterQuality(models.Model):
    ph = models.FloatField()
    hardness = models.FloatField()
    solids = models.FloatField()
    chloramines = models.FloatField()
    sulfate = models.FloatField()
    conductivity = models.FloatField()
    organic_carbon = models.FloatField()
    trihalomethanes = models.FloatField()
    turbidity = models.FloatField()
    potability = models.CharField(max_length=25, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name