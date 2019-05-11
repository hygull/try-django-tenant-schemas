from django.db import models
from tenant_schemas.models import TenantMixin
from customers.models import Client

class User(models.Model):
	name = models.CharField(max_length=50, default='Ram Bahadur', null=True, blank=True)
	username =  models.CharField(max_length=10, default='10minutes', null=True, blank=True)

	def __str__(self):
		return "User - %s" % self.name 


	# class Meta:
	# 	app_label = "users"
	# 	permissions = (
	# 		("view_user", "View User"),
	# 	)
