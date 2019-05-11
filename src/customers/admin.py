from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
	readonly_fields = ("schema_name", "domain_url",)

# admin.site.register(Client, ClientAdmin)
admin.site.register(Client, ClientAdmin)
