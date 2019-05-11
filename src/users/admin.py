from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    actions = None

    def has_add_permission(self, request):
    	# if request.get_host() == "my-domain.com"
    	# print(request.get_host())
    	# print(dir(request))
        return False

    def has_delete_permission(self, request, obj=None):

        return False

    # def save_model(self, request, obj, form, change):
    #     #Return nothing to make sure user can't update any data
    #     return False

    def has_change_permission(self, request, obj=None):
    	return False


admin.site.register(User)

# tenant_admin_site = admiun.AdminSite(name="tenant-admin")
# print(dir(UserAdmin))
# tenant_admin_site.register(User)




from django.contrib.admin import AdminSite
class UserAdminSite(AdminSite):
    site_header = "Users Admin"
    site_title = "Users site title"
    index_title = "Tenant Website"

user_admin_site = UserAdminSite(name='users_admin')

user_admin_site.register(User, UserAdmin)
# event_admin_site.register(Event)
# event_admin_site.register(EventHero)
# event_admin_site.register(EventVillain)