from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
#employeeApp import city, staate, country 
from employeeApp.models import city,state,country

# Create your models here.
STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)

Gender_Choices = (
	('male', 'Male'),
	('female', 'Female'),
)

Portfolio_Range = (
	('< 1 Lac','< 1 Lac'),
	('1 - 5 Lac','1 - 5 Lac'),
	('5 - 10 Lac','5 - 10 Lac'),
	('10 - 25 Lac','10 - 25 Lac'),
	('25 - 50 Lac','25 - 50 La'),
	('50 - 100 Lac','50 - 100 Lac'),
	('1 - 5 Crores','1 - 5 Crores'),
	('5 - 10 Crores','5 - 10 Crores'),
	('10 - 25 Crores','10 - 25 Crores'),
	('25 - 50 Crores','25 - 50 Crores'),
	('50 - 100 Crores','50 - 100 Crores'),
	('100 + Crores','100 + Crores'),
	)


Depository_Info = (
	('NSDL','NSDL'),
	('CDSL','CDSL'),
	)

# add by Shubham starts

AccountType_Info =(
	('Current','Current'),
	('Saving','Saving'),
	)

#end by Shubham


#
class investorPersonalDetails(models.Model): 
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerIPD', null=True, blank=True)
	name = models.CharField(max_length=1000, null=True, blank=True)
	email = models.EmailField(max_length = 254, null=True, blank=True)
	mobileNumber = models.BigIntegerField(null=True, blank=True)
	gender = models.CharField(max_length=50,choices=Gender_Choices, null=True, blank=True)
	panNumber = models.CharField(max_length=100, null=True, blank=True)
	uploadPan = models.FileField(upload_to ='investor/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	aadharNumber = models.CharField(max_length=100, null=True, blank=True)
	uploadAadhar = models.FileField(upload_to ='investor/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	address = models.TextField(null=True, blank=True)
	city =  models.ForeignKey(city, on_delete=models.SET_NULL, null=True, blank=True, related_name='cityIPD')
	pinCode = models.BigIntegerField(null=True,blank=True)
	state =  models.ForeignKey(state, on_delete=models.SET_NULL, null=True, blank=True, related_name='stateIPD')
	country =  models.ForeignKey(country, on_delete=models.SET_NULL, null=True, blank=True, related_name='countryIPD')
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorIPD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Investor Personal Details'


#starts by shubham
class lookingToInvestDetails(models.Model):
	name=models.CharField(max_length=1000,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='authorLTID',null= True,blank=True)
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	def __str__(self):
		return self.name or '--Name not provided'
	class Meta:
		verbose_name='Looking To Invest Details'
# ends by shubham

#
class investmentDetails(models.Model):
	profileOwner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerID',null=True,blank=True)
	presentPortfolio = models.CharField(max_length=50,choices=Portfolio_Range, null=True, blank=True)
	#fields needs to be add by Shubham starts
	secondaryMarket=models.BooleanField(null=True,blank=True)
	primaryMarket=models.BooleanField(null=True,blank=True)
	lookingToInvest=models.ManyToManyField(lookingToInvestDetails,blank=True)
	#fields needs to be add by Shubham ends 			
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorID', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return str(self.presentPortfolio) or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Investment Details'


#class investorAccountType(models.Model): #discard
#	name = models.CharField(max_length=250)
#	publish = models.DateTimeField(default=timezone.now)
#	created = models.DateTimeField(auto_now_add=True)
#	updated = models.DateTimeField(auto_now=True)
#	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#	def __str__(self):
#		return self.name or '--Name not provided--'

#	class Meta:
#		verbose_name_plural = 'Investor Account Type'

class investorBankDetails(models.Model):
	profileOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profileOwnerIBD', null=True, blank=True)
	bankName = models.CharField(max_length=1000)
	accountHolder = models.CharField(max_length=1000, null=True, blank=True)
	accountNumber = models.BigIntegerField(null=True,blank=True)

	#fields needs to be add by Shubham starts

	#accountType = models.ForeignKey(investorAccountType,related_name='accountTypeIBD',null=True, blank=True,on_delete=models.SET_NULL) #tuple
	accountType=models.CharField(max_length=10,choices=AccountType_Info,null=True,blank=True)
	#fields needs to be add by Shubham ends

	ifsc_Code = models.CharField(max_length=1000, null=True, blank=True)
	cancelledCheque = models.FileField(upload_to ='investor/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorIBD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.bankName or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Investor Bank Details'

#
class stockBrokerDetails(models.Model):
	name = models.CharField(max_length=1000, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Stock Broker Details'


class investorDMATDetails(models.Model):
	profileOwner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profileOwnerIDD')
	stockBroker = models.ForeignKey('stockBrokerDetails', on_delete=models.SET_NULL, related_name="stockBrokerIDD", null=True, blank=True)
	depository = models.CharField(max_length=10, choices=Depository_Info, null=True, blank=True)
	dmatClientMasterReport = models.FileField(upload_to ='investor/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	dpID = models.CharField(max_length=1000, null=True, blank=True)
	#fields type needs to be changed by Shubham starts
	clientID = models.BigIntegerField( null=True, blank=True) #field-type should be change
	#fields type needs to be changed by Shubham ends
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.dpID or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Investor DMAT Details'

class linkedInModel(models.Model):
	profileOwner =models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerIIM',null=True,blank=True)
	profileOwnerMM=models.ManyToManyField(User,blank=True,related_name='profileOwnerMMIIM')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	class Meta:
		verbose_name_plural = 'Iinked In Model'





# Create your models here.
