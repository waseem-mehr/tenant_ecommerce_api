
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import home_view

urlpatterns = [
    path('',home_view,name="home_view"),
    path('admin/', admin.site.urls),
    path('api/users/',include("users.urls")),
    path('api/addresses/',include("addresses.urls")),
    path("api/products/",include("products.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
