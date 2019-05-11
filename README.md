# try-django-tenant-schemas
A repository containing the source of a multi-tenant app (django-tenant-schemas is as a reference)

### Note

+ It is necessary to use a PostgreSQL database. django-tenant-schemas will ensure compatibility with the minimum required version of the latest Django release. At this time that is PostgreSQL 9.3, the minimum for Django 1.11. 

+ Refer [this](https://django-tenant-schemas.readthedocs.io/en/latest/use.html) for more info.

### What I used for this?

| Language/Framework/Platform | Version |
| --- | --- |
| Python | 3.6.7 |
| Django | 2.2 |
| OS | MAC OS Mojave 10.14.4 |

### Initial requirements 

**Note:** `pip install psycopg2` throws error in MAC OS Mojave (in my case), in your case 2 (it depends). Using version `psycopg2==2.7.3.2` works fine.


Here is the list basic initial dependencies (You may find it in .gitignore file).

```python
Django==2.2
psycopg2==2.7.3.2
pytz==2019.1
sqlparse==0.3.0
```

### Steps 

+ `(venv3.6.7.26apr) ➜  try-django-tenant-schemas git:(master) ✗ pip install django-tenant-schemas`


+ Make a change in settings.py like this.

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'tenantschemas5',
        'USER': 'hygull',
        'PASSWORD': 'hygull@123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

+ Add below as well.


```python
DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)
```

+ Add the below line to **MIDDLEWARE_CLASSES**/**MIDDLEWARE** (at very top so that each request can be set to use the correct schema).

`tenant_schemas.middleware.TenantMiddleware`

+ Add 2 more (optional). Finally, the structure will look something like this.

```

```

+ `python manage.py startapp customers`

+ Add the following code to **customers/models.py**.

```python
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
```


+ Add the following to **settings.py**

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

TENANT_MODEL = "customers.Client" # app.Model
```

+ Create 2 more apps named **users** and **books**.

+ Define models like as suggested below (add your own fields).

> books/models.py

```python
from django.db import models
from tenant_schemas.models import TenantMixin


class Author(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return "Author - %s" % self.name 


class Book(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	price = models.FloatField(default=0.0)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return "Book - %s" % str(self.pk)

```

> users/models.py

```python
from django.db import models
from tenant_schemas.models import TenantMixin


class User(models.Model):
	name = models.CharField(max_length=50, default='Ram Bahadur', null=True, blank=True)
	username =  models.CharField(max_length=10, default='10minutes', null=True, blank=True)

	def __str__(self):
		return "Author - %s" % self.name 

```

+ Register the related models in the **admin.py** e.g. `admin.site.register(Book)`.

+ Updated **settings.py** again with the following data.

```python
SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app
    'customers', # you must list the app where your tenant model resides in

    'django.contrib.contenttypes',

    # everything below here is optional
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
)


TENANT_APPS = (
    'django.contrib.contenttypes',

    # your tenant-specific apps
    "users",
    "books"
    # 'myapp.hotels',
    # 'myapp.houses',
)


# Application definition

INSTALLED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app

    'customers',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    # 'myapp.hotels',
    # 'myapp.houses',
    "users",
    "books"
)
```

+ Set default file storage (stop seeing warning).

> HINT: Set settings.DEFAULT_FILE_STORAGE to 'tenant_schemas.storage.TenantFileSystemStorage'

`DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'`

+ Run &raquo; `python manage.py makemigrations customers`


+ Run &raquo; `python manage.py migrate_schemas --shared`

+ Run &raquo; `python manage.py makemigrations users`

+ Run &raquo; `python manage.py makemigrations books`


### Sample output on Django shell

```bash
(venv3.6.7.26apr) ➜  src git:(master) ✗ python manage.py shell
Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 03:02:14) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
>>> 
>>> from customers.models import Client
>>> 
>>> # create your public tenant
>>> tenant = Client(domain_url='my-domain.com', # don't add your port or www here! on a local server you'll want to use localhost here
...                 schema_name='public',
...                 name='Schemas Inc.',
...                 paid_until='2016-12-05',
...                 on_trial=False)
>>> tenant.save()
>>> 
>>> tenants = Client.objects.all()
>>> tenants
<TenantQueryset [<Client: Client object (1)>]>
>>> 
>>> dir(tenants)
['__and__', '__bool__', '__class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_hints', '_batched_insert', '_chain', '_clone', '_combinator_query', '_create_object_from_params', '_db', '_earliest', '_extract_model_params', '_fetch_all', '_fields', '_filter_or_exclude', '_for_write', '_has_filters', '_hints', '_insert', '_iterable_class', '_iterator', '_known_related_objects', '_merge_known_related_objects', '_merge_sanity_check', '_next_is_sticky', '_populate_pk_values', '_prefetch_done', '_prefetch_related_lookups', '_prefetch_related_objects', '_raw_delete', '_result_cache', '_sticky_filter', '_update', '_validate_values_are_expressions', '_values', 'aggregate', 'all', 'annotate', 'as_manager', 'bulk_create', 'bulk_update', 'complex_filter', 'count', 'create', 'dates', 'datetimes', 'db', 'defer', 'delete', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'get', 'get_or_create', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'none', 'only', 'order_by', 'ordered', 'prefetch_related', 'query', 'raw', 'resolve_expression', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'using', 'values', 'values_list']
>>> 
>>> dir(tenants[0])
['DoesNotExist', 'Meta', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'auto_create_schema', 'auto_drop_schema', 'check', 'clean', 'clean_fields', 'create_schema', 'created_on', 'date_error_message', 'delete', 'domain_url', 'from_db', 'full_clean', 'get_deferred_fields', 'get_next_by_created_on', 'get_next_by_paid_until', 'get_previous_by_created_on', 'get_previous_by_paid_until', 'id', 'name', 'objects', 'on_trial', 'paid_until', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'schema_name', 'serializable_value', 'unique_error_message', 'validate_unique']
>>> 
>>> tenant1 = tenants[0]
>>> tenant1
<Client: Client object (1)>
>>> 
>>> tenant1.name
'Schemas Inc.'
>>> 
>>> tenant1.domain_url
'my-domain.com'
>>> 
>>> from customers.models import Client
>>> 
>>> # create your first real tenant
>>> tenant = Client(domain_url='tenant.my-domain.com', # don't add your port or www here!
...                 schema_name='tenant1',
...                 name='Fonzy Tenant',
...                 paid_until='2014-12-05',
...                 on_trial=True)
>>> tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!
[standard:tenant1] === Running migrate for schema tenant1
[standard:tenant1] Operations to perform:
[standard:tenant1]   Apply all migrations: admin, auth, books, contenttypes, customers, sessions, sites, users
[standard:tenant1] Running migrations:
[standard:tenant1]   Applying contenttypes.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying admin.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying admin.0002_logentry_remove_auto_add...
[standard:tenant1]  OK
[standard:tenant1]   Applying admin.0003_logentry_add_action_flag_choices...
[standard:tenant1]  OK
[standard:tenant1]   Applying contenttypes.0002_remove_content_type_name...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0002_alter_permission_name_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0003_alter_user_email_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0004_alter_user_username_opts...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0005_alter_user_last_login_null...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0006_require_contenttypes_0002...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0007_alter_validators_add_error_messages...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0008_alter_user_username_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0009_alter_user_last_name_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0010_alter_group_name_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0011_update_proxy_permissions...
[standard:tenant1]  OK
[standard:tenant1]   Applying books.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying customers.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying sessions.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying sites.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying sites.0002_alter_domain_unique...
[standard:tenant1]  OK
[standard:tenant1]   Applying users.0001_initial...
[standard:tenant1]  OK
>>> 
```

### Postgres terminal/Django shell test

1. Login

`psql -U hygull tenantschemas5`

2. List all tables with info

`SELECT * FROM information_schema.tables;`

3. List schemas

&raquo; `\dn`

```bash
tenantschemas5=# \dn
 List of schemas
  Name   | Owner  
---------+--------
 public  | hygull
 tenant1 | hygull
(2 rows)
```

4. Select specific schema (All tables)

> Make sure, you are not using double quotes around schema name like `"tenant"`, instead use `'tenant1'`.

&raquo; `tenantschemas5=# SELECT * FROM information_schema.tables where table_schema='tenant1';`

```bash
tenantschemas5=# SELECT * FROM information_schema.tables where table_schema='tenant1';

 table_catalog  | table_schema |     table_name      | table_type | self_referencing_column_name | reference_generation | user_defined_type_catalog | user_defined_type_schema | user_defined_type_name | is_insertable_into | is_typed | commit_action 
----------------+--------------+---------------------+------------+------------------------------+----------------------+---------------------------+--------------------------+------------------------+--------------------+----------+---------------
 tenantschemas5 | tenant1      | django_migrations   | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant1      | django_content_type | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant1      | books_author        | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant1      | books_book          | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant1      | users_user          | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
(5 rows)
```

Create another tenant named `tenant2` with domain `tenant2.my-domain.com` from Django shell

```bash
>>> from customers.models import Client
>>> 
>>> # create your first real tenant
>>> tenant = Client(domain_url='tenant2.my-domain.com', # don't add your port or www here!
...                 schema_name='tenant2',
...                 name='Fonzy Tenant',
...                 paid_until='2019-12-05',
...                 on_trial=True)
>>> tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!
[standard:tenant2] === Running migrate for schema tenant2
[standard:tenant2] Operations to perform:
[standard:tenant2]   Apply all migrations: admin, auth, books, contenttypes, customers, sessions, sites, users
[standard:tenant2] Running migrations:
[standard:tenant2]   Applying contenttypes.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying admin.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying admin.0002_logentry_remove_auto_add...
[standard:tenant2]  OK
[standard:tenant2]   Applying admin.0003_logentry_add_action_flag_choices...
[standard:tenant2]  OK
[standard:tenant2]   Applying contenttypes.0002_remove_content_type_name...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0002_alter_permission_name_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0003_alter_user_email_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0004_alter_user_username_opts...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0005_alter_user_last_login_null...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0006_require_contenttypes_0002...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0007_alter_validators_add_error_messages...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0008_alter_user_username_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0009_alter_user_last_name_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0010_alter_group_name_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0011_update_proxy_permissions...
[standard:tenant2]  OK
[standard:tenant2]   Applying books.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying customers.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying sessions.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying sites.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying sites.0002_alter_domain_unique...
[standard:tenant2]  OK
[standard:tenant2]   Applying users.0001_initial...
[standard:tenant2]  OK
>>> 
```

Now check it from Postgres terminal

`\dn`

```bash
tenantschemas5=# \dn
 List of schemas
  Name   | Owner  
---------+--------
 public  | hygull
 tenant1 | hygull
 tenant2 | hygull
(3 rows)
```

Now select all tables under schema named *tenant2* as follows.

`tenantschemas5=# SELECT * FROM information_schema.tables where table_schema='tenant2';`

```bash
tenantschemas5=# SELECT * FROM information_schema.tables where table_schema='tenant2';

 table_catalog  | table_schema |     table_name      | table_type | self_referencing_column_name | reference_generation | user_defined_type_catalog | user_defined_type_schema | user_defined_type_name | is_insertable_into | is_typed | commit_action 
----------------+--------------+---------------------+------------+------------------------------+----------------------+---------------------------+--------------------------+------------------------+--------------------+----------+---------------
 tenantschemas5 | tenant2      | django_migrations   | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant2      | django_content_type | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant2      | books_author        | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant2      | books_book          | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
 tenantschemas5 | tenant2      | users_user          | BASE TABLE |                              |                      |                           |                          |                        | YES                | NO       | 
(5 rows)

(END)
```

### Create super users for tenants

> password: Password@321

```bash
(venv3.6.7.26apr) ➜  src git:(master) ./manage.py createsuperuser --username=admin1 --schema=tenant1
Email address: admin@gmail.com
Password: 
Password (again): 
Superuser created successfully.
(venv3.6.7.26apr) ➜  src git:(master) ✗ ./manage.py createsuperuser --username=admin2 --schema=tenant2
Email address: admin2@gmail.com
Password: 
Password (again): 
Superuser created successfully.
(venv3.6.7.26apr) ➜  src git:(master) ✗ 
```


### Django rest framework

+ `pip install djangorestframework`

+ `pip install markdown`

+ `pip install django-filter`

+ Create **users/serializers.py**.

```python
from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields =  ("name", "username", )# ('id', 'title', 'code', 'linenos', 'language', 'style')	
        fields = "__all__"
```

+ Update **proj/urls.py**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls", namespace="users"))
]

```

+ Create **users/urls.py**.

```python
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('<int:pk>/', views.UserDetail.as_view(), name="users-detail"),
    path('', views.UserList.as_view(), name="users-list"),
]

```

### Postman API calls (Tenant 1)

1. `http://tenant.my-domain.com:9000/users/` (POST)

```python
	{
        "name": "Rishikesh Agrawani",
        "username": "Rishikesh"
    }
```

```python
    {
        "name": "Sanchit Garg",
        "username": "Sanchit"
    }
```

```python
    {
        "name": "Divyang Bissa",
        "username": "DivBis"
    }
```
	
2. `http://tenant.my-domain.com:9000/users/` (GET)

```bash
	[
	    {
	        "id": 1,
	        "name": "Rishikesh Agrawani",
	        "username": "Rishikesh"
	    },
	    {
	        "id": 3,
	        "name": "Divyang Bissa",
	        "username": "DivBis"
	    },
	    {
	        "id": 2,
	        "name": "Sanchit Garg",
	        "username": "Sanchit"
	    }
	]
```

### Postman API calls (Tenant 2)


1. `http://tenant2.my-domain.com:9000/users/` (POST)


```python
    {
        "id": 1,
        "name": "User1",
        "username": "User1Ten2"
    }
```

```python
    {
        "id": 2,
        "name": "User2",
        "username": "User2Ten2"
    }
```

2. `http://tenant2.my-domain.com:9000/users/` (GET)

```python
[
    {
        "id": 1,
        "name": "User1",
        "username": "User1Ten2"
    },
    {
        "id": 2,
        "name": "User2",
        "username": "User2Ten2"
    }
]
```

### Make API calls to create, update, get users.

Now we can login to postgres and check.

> DATABASE: **tenantschemas5**

```bash
tenantschemas5=# SELECT * FROM tenant1.users_user;
 id |        name        | username  
----+--------------------+-----------
  1 | Rishikesh Agrawani | Rishikesh
  3 | Divyang Bissa      | DivBis
  2 | Sanchit Garg       | Sanchit
(3 rows)

tenantschemas5=# SELECT * FROM tenant2.users_user;
 id | name  | username  
----+-------+-----------
  1 | User1 | User1Ten2
  2 | User2 | User2Ten2
(2 rows)
```


### Terminal logs

```bash
--------------------------------------------------
[GET SINGLE USER]  tenant.my-domain.com:9000
--------------------------------------------------
[26/Apr/2019 11:50:29] "GET /users/2/ HTTP/1.1" 200 51
--------------------------------------------------
[CREATE USER]  tenant2.my-domain.com:9000
--------------------------------------------------
{'name': 'User1', 'username': 'User1Ten2'}
User - User1
[26/Apr/2019 11:51:56] "POST /users/ HTTP/1.1" 200 106
--------------------------------------------------
[CREATE USER]  tenant2.my-domain.com:9000
--------------------------------------------------
{'name': 'User2', 'username': 'User2Ten2'}
User - User2
[26/Apr/2019 11:52:10] "POST /users/ HTTP/1.1" 200 106
--------------------------------------------------
[GET ALL USERS]  tenant2.my-domain.com:9000
--------------------------------------------------
[26/Apr/2019 11:52:18] "GET /users/ HTTP/1.1" 200 95
--------------------------------------------------
[GET ALL USERS]  tenant.my-domain.com:9000
--------------------------------------------------
[26/Apr/2019 11:52:37] "GET /users/ HTTP/1.1" 200 165
--------------------------------------------------
[GET ALL USERS]  tenant2.my-domain.com:9000
--------------------------------------------------
[26/Apr/2019 12:03:19] "GET /users/ HTTP/1.1" 200 95

```



Now, add **LOGGING** to settings.py

```python
LOGGING = {
    'filters': {
        'tenant_context': {
            '()': 'tenant_schemas.log.TenantContextFilter'
        },
    },
    'formatters': {
        'tenant_context': {
            'format': '[%(schema_name)s:%(domain_url)s] '
            '%(levelname)-7s %(asctime)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'filters': ['tenant_context'],
        },
    },
}
```


Now do the following change in **settings.py**.

```python

SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app
    'customers', # you must list the app where your tenant model resides in

    # 'django.contrib.contenttypes',

    # everything below here is optional
    # 'django.contrib.auth',
    # 'django.contrib.sessions',
    # 'django.contrib.sites',
    # 'django.contrib.messages',
    # 'django.contrib.admin',
)


TENANT_APPS = (
    # your tenant-specific apps
    "users",
    "books",
    # "users.apps.UsersConfig",
    # "books.apps.BooksConfig",
    # 'myapp.hotels',
    # 'myapp.houses',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

)


# Application definition

INSTALLED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app

    'customers',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    # 'myapp.hotels',
    # 'myapp.houses',
    "users",
    "books"
    # "users.apps.UsersConfig",
    # "books.apps.BooksConfig",
    # "rest_framework"
)
```

On *psql** terminal, type the following commands to create a new database.

```bash
tenantschemas5=# \c tenantschemas8;
You are now connected to database "tenantschemas8" as user "hygull".
tenantschemas8=# 
tenantschemas8=# \dn
 List of schemas
  Name   | Owner  
---------+--------
 public  | hygull
 tenant1 | hygull
 tenant2 | hygull
(3 rows)

tenantschemas8=# \dt
              List of relations
 Schema |       Name        | Type  | Owner  
--------+-------------------+-------+--------
 public | customers_client  | table | hygull
 public | django_migrations | table | hygull
(2 rows)

tenantschemas8=# SELECT * FROM information_schema.tables where table_schema='tenant2';
tenantschemas8=# SELECT * FROM tenant1.django_site;
 id |   domain    |    name     
----+-------------+-------------
  1 | example.com | example.com
(1 row)

tenantschemas8=# SELECT * FROM tenant2.django_site;
 id |   domain    |    name     
----+-------------+-------------
  1 | example.com | example.com
(1 row)

tenantschemas8=# INSERT INTO tenant1.django_site VALUES (2, 'tenant1.my-domain.com', 'tenant1.my-domain.com');
INSERT 0 1
tenantschemas8=# INSERT INTO tenant2.django_site VALUES (2, 'tenant2.my-domain.com', 'tenant2.my-domain.com');
INSERT 0 1
tenantschemas8=# 
```

Then update the **DATABASES** entry to below.

```python
DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        # ...
    }
}
```

And open python shell and execute the following statements.

```python
>>> from customers.models import Client
>>> 
>>> from customers.models import Client
>>> tenant = Client(domain_url='my-domain.com', # don't add your port or www here! on a local server you'll want to use localhost here
...                 schema_name='public',
...                 name='Schemas Inc.',
...                 paid_until='2016-12-05',
...                 on_trial=False)
>>> tenant.save()
```

```python
>>> 
>>> tenant = Client(domain_url='tenant1.my-domain.com', # don't add your port or www here!
...                 schema_name='tenant1',
...                 name='Fonzy Tenant',
...                 paid_until='2019-12-05',
...                 on_trial=True)
>>> tenant.save()
[standard:tenant1] === Running migrate for schema tenant1
[standard:tenant1] Operations to perform:
[standard:tenant1]   Apply all migrations: admin, auth, books, contenttypes, customers, sessions, sites, users
[standard:tenant1] Running migrations:
[standard:tenant1]   Applying contenttypes.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying admin.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying admin.0002_logentry_remove_auto_add...
[standard:tenant1]  OK
[standard:tenant1]   Applying admin.0003_logentry_add_action_flag_choices...
[standard:tenant1]  OK
[standard:tenant1]   Applying contenttypes.0002_remove_content_type_name...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0002_alter_permission_name_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0003_alter_user_email_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0004_alter_user_username_opts...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0005_alter_user_last_login_null...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0006_require_contenttypes_0002...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0007_alter_validators_add_error_messages...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0008_alter_user_username_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0009_alter_user_last_name_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0010_alter_group_name_max_length...
[standard:tenant1]  OK
[standard:tenant1]   Applying auth.0011_update_proxy_permissions...
[standard:tenant1]  OK
[standard:tenant1]   Applying books.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying customers.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying sessions.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying sites.0001_initial...
[standard:tenant1]  OK
[standard:tenant1]   Applying sites.0002_alter_domain_unique...
[standard:tenant1]  OK
[standard:tenant1]   Applying users.0001_initial...
[standard:tenant1]  OK
>>> 
```

```python
>>> tenant = Client(domain_url='tenant2.my-domain.com', # don't add your port or www here!
...                 schema_name='tenant2',
...                 name='Fonzy Tenant',
...                 paid_until='2019-12-10',
...                 on_trial=True)
>>> 
>>> tenant.save()
[standard:tenant2] === Running migrate for schema tenant2
[standard:tenant2] Operations to perform:
[standard:tenant2]   Apply all migrations: admin, auth, books, contenttypes, customers, sessions, sites, users
[standard:tenant2] Running migrations:
[standard:tenant2]   Applying contenttypes.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying admin.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying admin.0002_logentry_remove_auto_add...
[standard:tenant2]  OK
[standard:tenant2]   Applying admin.0003_logentry_add_action_flag_choices...
[standard:tenant2]  OK
[standard:tenant2]   Applying contenttypes.0002_remove_content_type_name...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0002_alter_permission_name_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0003_alter_user_email_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0004_alter_user_username_opts...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0005_alter_user_last_login_null...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0006_require_contenttypes_0002...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0007_alter_validators_add_error_messages...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0008_alter_user_username_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0009_alter_user_last_name_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0010_alter_group_name_max_length...
[standard:tenant2]  OK
[standard:tenant2]   Applying auth.0011_update_proxy_permissions...
[standard:tenant2]  OK
[standard:tenant2]   Applying books.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying customers.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying sessions.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying sites.0001_initial...
[standard:tenant2]  OK
[standard:tenant2]   Applying sites.0002_alter_domain_unique...
[standard:tenant2]  OK
[standard:tenant2]   Applying users.0001_initial...
[standard:tenant2]  OK
>>>
```

Create superusers with (Common password: `Password@123`)

```bash
(venv3.6.7.26apr) ➜  src git:(master) ✗ ./manage.py createsuperuser --username=admin1 --schema=tenant1
Email address: admin1@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```

```bash
(venv3.6.7.26apr) ➜  src git:(master) ✗ ./manage.py createsuperuser --username=admin2 --schema=tenant2
Email address: admin2@gmail.com
Password: 
Password (again): 
Superuser created successfully.
(venv3.6.7.26apr)
```


# References

- [x] [https://django-tenant-schemas.readthedocs.io/en/latest/install.html](https://django-tenant-schemas.readthedocs.io/en/latest/install.html)

- [x] [http://books.agiliq.com/projects/django-multi-tenant/en/latest/](http://books.agiliq.com/projects/django-multi-tenant/en/latest/) 