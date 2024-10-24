from django.db import models


class Disaster(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
