from django.db import models



class Service(models.Model):
    name = models.CharField(max_length=80)
    desc = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name