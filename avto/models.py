from django.db import models

class Avtomobile(models.Model):
    model = models.CharField(max_length=70, blank=True)
    year = models.IntegerField(null=True, blank=True, default=200)
    price = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=20, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self) -> str:
        return self.model