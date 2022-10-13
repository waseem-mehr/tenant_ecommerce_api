from django.db import models
from addresses.models import Country,State,City
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.

class Categorey(models.Model):
    name = models.CharField(max_length=55,null=False,blank=False)

    def __str__(self):
        return "{}".format(self.name)


class Brand(models.Model):
    name = models.CharField(max_length=55,null=False,blank=False)

    def __str__(self):
        return "{}".format(self.name)


class Products(models.Model):
    id  = models.CharField(primary_key=True,max_length=255,null=False,blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255,null=False,blank=False)
    categorey = models.ForeignKey(Categorey,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)
