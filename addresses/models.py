from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=55,null=False,blank=False)

    def __str__(self):
        return "{}".format(self.name)


class State(models.Model):
    name = models.CharField(max_length=55,null=False,blank=False)

    def __str__(self):
        return "{}".format(self.name)


class City(models.Model):
    name = models.CharField(max_length=55,null=False,blank=False)

    def __str__(self):
        return "{}".format(self.name)