

from django.urls import path
from .views import *

urlpatterns = [
   
    path('get-user-data/',GetUserAPI.as_view(),name="get_user"),
     path('get-user-business/',GetUserBusinessAPI.as_view(),name="get_user_business"),
     path('signup/',SignupView.as_view(),name="signup"),
]
