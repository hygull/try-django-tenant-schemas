from customers.models import Client

# Public Tenant
tenant = Client(domain_url='my-domain.com', # don't add your port or www here! on a local server you'll want to use localhost here
                schema_name='public',
                name='Schemas Inc.',
                paid_until='2016-12-05',
                on_trial=False)
tenant.save()

# Tenant 1
tenant1 = Client(domain_url='tenant1.my-domain.com', # don't add your port or www here!
                schema_name='tenant1',
                name='Fonzy Tenant',
                paid_until='2019-12-05',
                on_trial=True)
tenant1.save()

# Tenant 2
tenant2 = Client(domain_url='tenant2.my-domain.com', # don't add your port or www here!
                schema_name='tenant2',
                name='Fonzy Tenant',
                paid_until='2019-12-10',
                on_trial=True)
tenant2.save()