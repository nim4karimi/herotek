from django.db import models



class Service(models.Model):
    name = models.CharField(max_length=80)
    desc = models.TextField()
    pic = models.FileField(upload_to='pic/', blank=True, null=True)
    date = models.DateTimeField()
 
    def __str__(self):
        return self.name


class Prod(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    body = models.TextField()
    pic = models.FileField(upload_to='pic/', blank=True, null=True)

    def __str__(self):
        return self.name
