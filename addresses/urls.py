

from django.urls import path
from .views import *

urlpatterns = [
        path('get-cities/',GetCitiesAPI.as_view(),name="get_cities"),
        path('get-states/',GetStatesAPI.as_view(),name="get_states"),
        path('get-countries/',GetCountriesAPI.as_view(),name="get_countries"),
    ]
