from django.db import models

# Create your models here.


class ApiTest (models.Model):
    name = models.CharField(max_length=100)
    decription = models.CharField(max_length=300)
    pic = models.FileField(upload_to='pic/', blank=True, null=True)
    email = models.EmailField(blank=True , null=True)
    phone = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True)

    def __str__(self):
        return self.name
