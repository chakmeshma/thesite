from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
