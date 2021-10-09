from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User 
from employeeApp.models import city,state,country
# Create your models herecontact

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)

AccountType_Info =(
	('Current','Current'),
	('Saving','Saving'),
	)

Depository_Info = (
	('NSDL','NSDL'),
	('CDSL','CDSL'),
	)

Assets_Range = (
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
Transfer_Type=(
	('Physical DIS','PhysicalDIS'),
	('Online eDIS','Online eDIS'),
	('NSDL Speed-e','CDSL Easi'),
	('CDSL Easi','CDSL Easi')
	)

#SEBI_Type=(
#	('Alternate investment found','Alternate investment found'),
#	('FPI/FII/QFI','FPI/FII/QFI'),
#	('Foreign Venture Capital Fnd','Foreign Venture Capital Fnd'),
#	('Indian Venture Capital Fund','Indian Venture Capital Fund'),
#	('Investment Adviser','Investment Adviser'),
#	('Mutual Fund','Mutual Fund'),
#	('Stock Broker','Stock Broker'),
#	('Portfolio Managers','Portfolio Managers'),
#	('Syndicate Banks','Syndicate Banks'),
#	)

																							
"""  Personal Detail Model"""

class institutionalPersonalDetails(models.Model):
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerIPDI', null=True, blank=True)
	contactPersonName=models.CharField(max_length=1000,null=True,blank=True)
	email=models.EmailField(max_length=254,null=True,blank=True) 
	mobileNumber=models.BigIntegerField(null=True,blank=True)
	role=models.CharField(max_length=1000,null=True,blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorIPDI', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.contactPersonName or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Institutional Personal Details'	
""" Company Detail Model """

class registerWithSEBIDetails(models.Model):
	name=models.CharField(max_length=1000,null=True,blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorRWSD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Register With SEBI Details'

class institutionalCompanyDetails(models.Model):
	profileOwner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerICD',null=True,blank=True)
	nameOfOrganization=models.CharField(max_length=1000,null=True,blank=True)
	companyAddress=models.TextField(null=True,blank=True)
	city =  models.ForeignKey(city, on_delete=models.SET_NULL, null=True, blank=True, related_name='cityICD')
	pinCode = models.BigIntegerField(null=True,blank=True)
	state =  models.ForeignKey(state, on_delete=models.SET_NULL, null=True, blank=True, related_name='stateICD')
	country =  models.ForeignKey(country, on_delete=models.SET_NULL, null=True, blank=True, related_name='countryICD')
	companyWebsiteURL=models.URLField(max_length=1000,null=True,blank=True)
	#registerWithSEBI=models.CharField(max_length=50,choices='SEBI_Type',null=True,blank=True)
	registerWithSEBI = models.ForeignKey('registerWithSEBIDetails', on_delete=models.SET_NULL, related_name="registerWithSEBIICD", null=True, blank=True)
	SEBIRegistration=models.CharField(max_length=1000,null=True,blank=True)
	panCardNumber=models.CharField(max_length=1000,null=True,blank=True)
	panCard=models.FileField(upload_to ='institutional/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorICD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.nameOfOrganization or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Institutional Company Details'

""" Investment Detail Model"""

class lookingForPrivateCompany(models.Model):
	name=models.CharField(max_length=1000,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='authorLFPCI',null=True,blank=True)
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	def __str__(self):
		return self.name or '--Name not provided'
	class Meta:
		verbose_name='Looking For Private Company'

class lookingToInvestDetails(models.Model):
	name=models.CharField(max_length=1000,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='authorLTIDI',null= True,blank=True)
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	def __str__(self):
		return self.name or '--Name not provided'
	class Meta:
		verbose_name='Looking To Invest Details'

class majorSectorDetails(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='authorMSD',null= True,blank=True)
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	def __str__(self):
		return self.name or '--Name not provided'
	class Meta:
		verbose_name='Major Sector Details'

class institutionalInvestmentDetails(models.Model):
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerIID', null=True, blank=True)
	assetsYouAreManaging=models.CharField(max_length=50,choices=Assets_Range,null=True,blank=True)
	majorSector=models.ForeignKey('majorSectorDetails',on_delete=models.SET_NULL,related_name='majorSectorIID',null=True,blank=True)
	secondaryMarket=models.BooleanField(null=True,blank=True)
	primaryMarket=models.BooleanField(null=True,blank=True)
	lookingToInvest=models.ManyToManyField(lookingToInvestDetails,blank=True) 
	lookingForPrivateCompany=models.ManyToManyField(lookingForPrivateCompany,blank=True)
    #majorSector=models.CharField(max_length=1000,null=True,blank=True)
    #majorSector = models.ForeignKey('majorSectorDetails', on_delete=models.SET_NULL, related_name="majorSectorIID", null=True, blank=True)			
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorIID', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return str(self.assetsYouAreManaging) or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Institutional Investment Details'

""" Bank Datail Model"""

class institutionalBankDetails(models.Model):
	profileOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profileOwnerIBDI', null=True, blank=True)
	bankName = models.CharField(max_length=1000)
	accountHolder = models.CharField(max_length=1000, null=True, blank=True)
	accountNumber = models.BigIntegerField(null=True,blank=True)
	accountType=models.CharField(max_length=10,choices=AccountType_Info,null=True,blank=True)
	ifsc_Code = models.CharField(max_length=1000, null=True, blank=True)
	cancelledCheque = models.FileField(upload_to ='institutional/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorIBDI', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.bankName or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Institutional Bank Details'

""" Demat details model"""

class stockBrokerDetails(models.Model):
	name = models.CharField(max_length=1000, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorSBDI', null=True, blank=True)

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Stock Broker Details'


class institutionalDematDetails(models.Model):
	profileOwner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profileOwnerIDDI')
	stockBroker = models.ForeignKey('stockBrokerDetails', on_delete=models.SET_NULL, related_name="stockBrokerIDD", null=True, blank=True)
	depository = models.CharField(max_length=10,choices=Depository_Info, null=True, blank=True)
	dmatClientMasterReport = models.FileField(upload_to ='investor/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	dpID = models.CharField(max_length=1000, null=True, blank=True)
	clientID = models.BigIntegerField( null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.dpID or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Institutional Demat Details'

""" Transfer Facility Details Model"""

class transferFacilityDetails(models.Model):
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerTFD', null=True, blank=True)
	transferShares=models.CharField(max_length=50, choices=Transfer_Type,null=True,blank=True)
	transferFileProof=models.FileField(upload_to='institutional/documents/',null=True,blank=True,validators=[FileExtensionValidator(['pdf'])])
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.transferShares or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Transfer Shares Details'

#class linkedInModel(models.Model):
#	profileOwner =models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerIIM',null=True,blank=True)
#	profileOwnerMM=models.ManyToManyField(User,blank=True,related_name='profileOwnerMMIIM')
#	publish = models.DateTimeField(default=timezone.now)
#	created = models.DateTimeField(auto_now_add=True)
#	updated = models.DateTimeField(auto_now=True)
#	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#	class Meta:
#		verbose_name_plural = 'Iinked In Model'




