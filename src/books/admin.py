from django.contrib import admin
from .models import Book, Author
# Register your models here.
from users.admin import user_admin_site

class CommonPermission(admin.ModelAdmin):
	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

	def has_change_permission(self, request, obj=None):
		return False

@admin.register(Book, site=user_admin_site)
class BookAdmin(CommonPermission):
	pass



@admin.register(Author, site=user_admin_site)
class AuthorAdmin(CommonPermission):
	pass


