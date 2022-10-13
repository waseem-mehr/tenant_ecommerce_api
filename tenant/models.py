from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import DomainMixin, TenantMixin
from django.contrib.auth import get_user_model
User=get_user_model()

class Tenant(TenantMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True, blank=True)
    
    auto_create_schema = True
    auto_drop_schema = True

    def __str__(self):
        return "{}".format(self.user)


class Domain(DomainMixin):
    pass