from django.db import models
from tenant_schemas.models import TenantMixin

class Client(TenantMixin):
    """
    TenantMixin has 2 fields
        - domain_url
        - schema_name
    """

    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


    def __str__(self):
        return 'Client - ' + self.name
    

class Credential(models.Model):
    arn_user_id = models.CharField(max_length=10)
    appln_id = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.arn_user_id} | {self.appln_id} | {self.password}"