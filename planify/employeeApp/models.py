from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from django.core.validators import FileExtensionValidator


STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)

class city(models.Model):
	name=models.CharField(max_length=50,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True, related_name='authorC')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'City'

class state(models.Model):
	name=models.CharField(max_length=50,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True, related_name='authorS')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'State'

class country(models.Model):
	name=models.CharField(max_length=50,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True, related_name='authorCC')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Country'

# Create your models here.
