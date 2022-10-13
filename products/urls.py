

from django.urls import path
from .views import *

urlpatterns = [
        path('get-products/',GetProductsAPI.as_view(),name="get_products"),
       path('get-business-products/',GetProductsAPI.as_view(),name="get_products"),
        
        path('get-brand/<int:id>/',BrandAPI.as_view(),name="get_brand"),
        path('delete-brand/<int:id>/',BrandAPI.as_view(),name="delete_brand"),
        path('update-brand/<int:id>/',BrandAPI.as_view(),name="update_brand"),
        path('create-brand/',BrandAPI.as_view(),name="create_brand"),
       
        path('get-categorey/<int:id>/',CategoreyAPI.as_view(),name="get_categorey"),
        path('delete-categorey/<int:id>/',CategoreyAPI.as_view(),name="delete_categorey"),
        path('update-categorey/<int:id>/',CategoreyAPI.as_view(),name="update_categorey"),
        path('create-categorey/',CategoreyAPI.as_view(),name="create_categorey"),
       

       path('delete-product/<int:id>/',ProductAPI.as_view(),name="delete_product"),
        path('update-product/<int:id>/',ProductAPI.as_view(),name="update_product"),
        path('create-product/',ProductAPI.as_view(),name="create_product"),
       
    ]
