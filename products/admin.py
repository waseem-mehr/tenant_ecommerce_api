from django.contrib import admin
from .models import Products,Categorey,Brand
# Register your models here.
admin.site.register(Categorey)
admin.site.register(Brand)
admin.site.register(Products)
