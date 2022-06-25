from django.db import models


# Create your models here.
class Asset(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    explorer = models.URLField(max_length=200)

    def __str__(self):
        return self.name