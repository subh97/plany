from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from employeeApp.models import city,state,country

class planifyHeadQuarterContactUs(models.Model):
	title = models.CharField(max_length=1000, null=True, blank=True)
	content = models.TextField(null=True, blank=True)
	image_1 = models.ImageField(upload_to='website/contactUs', null=True, blank=True)
	image_2 = models.ImageField(upload_to='website/contactUs', null=True, blank=True)
	image_3 = models.ImageField(upload_to='website/contactUs', null=True, blank=True)
	city=models.ForeignKey(city, on_delete=models.SET_NULL, null=True, blank=True, related_name='statePHQCU')
	state = models.ForeignKey(state, on_delete=models.SET_NULL, null=True, blank=True, related_name='statePHQCU')
	address=models.TextField(null=True,blank=True)
	mobileNumber=models.BigIntegerField(null=True,blank=True)
	email=models.EmailField(null=True,blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorPhcus', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.title or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Planify Contact Us Page - OUR HEADQUARTER'

#
class planifyFranchiseeContactUs(models.Model):
	name = models.CharField(max_length=1000, null=True, blank=True)
	phoneNo_1 = models.BigIntegerField(null=True, blank=True)
	phoneNo_2 = models.BigIntegerField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	city = models.ForeignKey(city, on_delete=models.SET_NULL, null=True, blank=True, related_name='statePFCUS')
	state = models.ForeignKey(state, on_delete=models.SET_NULL, null=True, blank=True, related_name='statePFCUS')
	country = models.ForeignKey(country, on_delete=models.SET_NULL, null=True, blank=True, related_name='countryPFCUS')
	backgroundImage = models.ImageField(upload_to='website/contactUs', null=True, blank=True)
	partnerImage = models.ImageField(upload_to='website/contactUs', null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorPFCUS', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Planify Contact Us Page - OUR FRANCHISEE'

class planifyEliteChannelPartner(models.Model):
	name = models.CharField(max_length=1000, null=True, blank=True)
	phoneNo_1 = models.BigIntegerField(null=True, blank=True)
	phoneNo_2 = models.BigIntegerField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	city = models.ForeignKey(city, on_delete=models.SET_NULL, null=True, blank=True, related_name='statePECP')
	state = models.ForeignKey(state, on_delete=models.SET_NULL, null=True, blank=True, related_name='statePECP')
	country = models.ForeignKey(country, on_delete=models.SET_NULL, null=True, blank=True, related_name='countryPECP')
	backgroundImage = models.ImageField(upload_to='website/contactUs', null=True, blank=True)
	partnerImage = models.ImageField(upload_to='website/contactUs', null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorPECP', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Planify Contact Us Page - Elite Channel Partner '


#class planifyGetInTouchContactUs(models.Model):
#	email = models.EmailField(null=True, blank=True)
#	phoneNo = models.BigIntegerField(null=True, blank=True)
##	address_Line_2 = models.TextField(null=True, blank=True)
#	tag_Line = models.CharField(max_length=1000, null=True, blank=True)
#	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorPGITCUS', null=True, blank=True)
#	publish = models.DateTimeField(default=timezone.now)
#	created = models.DateTimeField(auto_now_add=True)
#	updated = models.DateTimeField(auto_now=True)
#	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#	def __str__(self):
#		return self.email or '--Name not provided--'

#	class Meta:
#		verbose_name_plural = 'Planify Contact Us Page - Get In Touch'	


class planifyLetsTalkContactUs(models.Model):
	name = models.CharField(max_length=1000, null=True, blank=True)
	phoneNo = models.BigIntegerField(null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorLTCUS', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Planify Contact Us Page - Lets Talk'	
