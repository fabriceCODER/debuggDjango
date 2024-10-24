from django.db import models
from disaster.models import Disaster

class Resource(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
