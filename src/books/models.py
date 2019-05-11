from django.db import models
from tenant_schemas.models import TenantMixin


class Author(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)

	# class Meta:
	# 	permissions = (
	# 		("view_author", "View Author"),
	# 	)

	def __str__(self):
		return "Author | %s" % self.name 


class Book(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	price = models.FloatField(default=0.0)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return "Book - %s" % str(self.pk) + " by | " + self.author.name


class Pincode(models.Model):
	officename = models.CharField(max_length=255, null=True, blank=True, default='')
	pincode = models.CharField(max_length=255, null=True, blank=True, default='')
	officetype = models.CharField(max_length=255, null=True, blank=True, default='')
	deliverystatus = models.CharField(max_length=255, null=True, blank=True, default='')
	divisionname = models.CharField(max_length=255, null=True, blank=True, default='')
	regionname = models.CharField(max_length=255, null=True, blank=True, default='')
	circlename = models.CharField(max_length=255, null=True, blank=True, default='')
	taluk = models.CharField(max_length=255, null=True, blank=True, default='')
	districtname = models.CharField(max_length=255, null=True, blank=True, default='')
	statename = models.CharField(max_length=255, null=True, blank=True, default='')

	def __str__(self):
		return pincode

