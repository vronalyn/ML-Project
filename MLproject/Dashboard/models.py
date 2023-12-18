from django.db import models

# Create your models here.

class WaterPotability(models.Model):
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
        return self.potability
    

class AdSales(models.Model):
    TV_Ad_Budget = models.FloatField()
    Radio_Ad_Budget = models.FloatField()
    Newspaper_Ad_Budget = models.FloatField()
    Sales = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return (
            f"{self.TV_Ad_Budget} - "
            f"{self.Radio_Ad_Budget} - "
            f"{self.Newspaper_Ad_Budget} - "
            f"{self.Sales} - "
            f"{self.date}"
        )