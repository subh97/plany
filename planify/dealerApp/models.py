from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User 
from employeeApp.models import city,state,country

Network_Types=(
	('Unlisted Share Dealer','Unlisted Share Dealer'),
	('Unlisted PreIPO Dealer','Unlisted PreIPO Dealer'),
	('others','others'),
	)

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)

Gender_Choices = (
	('male', 'Male'),
	('female', 'Female'),
)

Transfer_Type=(
	('Physical DIS','PhysicalDIS'),
	('Online eDIS','Online eDIS'),
	('NSDL Speed-e','CDSL Easi'),
	('CDSL Easi','CDSL Easi')
	)


Depository_Info = (
	('NSDL','NSDL'),
	('CDSL','CDSL'),
	)

AccountType_Info =(
	('Current','Current'),
	('Saving','Saving'),
	)

class dealersNetworkDetails(models.Model):
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerDND', null=True, blank=True)
	networkPart=models.CharField(max_length=100,choices=Network_Types,default='draft')
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorDND', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.networkPartOf or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Network Part Of Details'

#personal detail
class dealerPersonalDetail(models.Model): 
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerDPD', null=True, blank=True)
	name = models.CharField(max_length=1000, null=True, blank=True)
	email = models.EmailField(max_length = 254, null=True, blank=True)
	mobileNumber = models.BigIntegerField(null=True, blank=True)
	gender = models.CharField(max_length=50,choices=Gender_Choices, null=True, blank=True)
	panNumber = models.CharField(max_length=100, null=True, blank=True)
	uploadPan = models.FileField(upload_to ='dealer/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	aadharNumber = models.CharField(max_length=100, null=True, blank=True)
	uploadAadhar = models.FileField(upload_to ='dealer/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	address = models.TextField(null=True, blank=True)
	city =  models.ForeignKey(city, on_delete=models.SET_NULL, null=True, blank=True, related_name='cityDPD')
	pinCode = models.BigIntegerField(null=True,blank=True)
	state =  models.ForeignKey(state, on_delete=models.SET_NULL, null=True, blank=True, related_name='stateDPD')
	country =  models.ForeignKey(country, on_delete=models.SET_NULL, null=True, blank=True, related_name='countryDPD')
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorDPD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Dealer Personal Detail'

class registerWithSEBIDetail(models.Model):
	name=models.CharField(max_length=1000,null=True,blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorRWSDD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Register With SEBI Detail'

class dealerCompanyDetail(models.Model):
	profileOwner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerDCD',null=True,blank=True)
	nameOfOrganization=models.CharField(max_length=1000,null=True,blank=True)
	companyAddress=models.TextField(null=True,blank=True)
	city =  models.ForeignKey(city, on_delete=models.SET_NULL, null=True, blank=True, related_name='cityDCD')
	pinCode = models.BigIntegerField(null=True,blank=True)
	state =  models.ForeignKey(state, on_delete=models.SET_NULL, null=True, blank=True, related_name='stateDCD')
	country =  models.ForeignKey(country, on_delete=models.SET_NULL, null=True, blank=True, related_name='countryDCD')
	companyWebsiteURL=models.URLField(max_length=1000,null=True,blank=True)
	registerWithSEBI = models.ForeignKey('registerWithSEBIDetail', on_delete=models.SET_NULL, related_name="registerWithSEBIDCD", null=True, blank=True)
	SEBIRegistration=models.CharField(max_length=1000,null=True,blank=True)
	panCardNumber=models.CharField(max_length=1000,null=True,blank=True)
	panCard=models.FileField(upload_to ='dealer/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorDCD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.nameOfOrganization or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Dealer Company Detail'

class dealerBankDetail(models.Model):
	profileOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profileOwnerDBD', null=True, blank=True)
	bankName = models.CharField(max_length=1000)
	accountHolder = models.CharField(max_length=1000, null=True, blank=True)
	accountNumber = models.BigIntegerField(null=True,blank=True)
	accountType=models.CharField(max_length=10,choices=AccountType_Info,null=True,blank=True)
	ifsc_Code = models.CharField(max_length=1000, null=True, blank=True)
	cancelledCheque = models.FileField(upload_to ='dealer/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorDBD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.bankName or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Dealer Bank Detail'


class stockBrokerDetail(models.Model):
	name = models.CharField(max_length=1000, null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorSBD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Stock Broker Detail'


class dealerDematDetail(models.Model):
	profileOwner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profileOwnerDDD')
	stockBroker = models.ForeignKey('stockBrokerDetail', on_delete=models.SET_NULL, related_name="stockBrokerDDD", null=True, blank=True)
	depository = models.CharField(max_length=10,choices=Depository_Info, null=True, blank=True)
	dmatClientMasterReport = models.FileField(upload_to ='dealer/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	dpID = models.CharField(max_length=1000, null=True, blank=True)
	clientID = models.BigIntegerField( null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorDDD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.dpID or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Dealer Demat Detail'

class dealerTransferFacilityDetail(models.Model):
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerDTFD', null=True, blank=True)
	transferShares=models.CharField(max_length=50, choices=Transfer_Type,null=True,blank=True)
	transferFileProof=models.FileField(upload_to='dealer/documents/',null=True,blank=True,validators=[FileExtensionValidator(['pdf'])])
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorDTFD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.transferShares or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Dealer Transfer Shares Detail'

class linkedInModels(models.Model):
	profileOwner =models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerIIMS',null=True,blank=True)
	profileOwnerMM=models.ManyToManyField(User,blank=True,related_name='profileOwnerMMIIMS')
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorIIMS', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	class Meta:
		verbose_name_plural = 'Iinked In Models'