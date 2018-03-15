from django.db import models

# Create your models here.


class ApiTest (models.Model):
    name = models.CharField(max_length=100)
    decription = models.CharField(max_length=300)


    def __str__(self):
        return self.name