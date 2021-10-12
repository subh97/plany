from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from employeeApp.models import city,state,country


Gender_Choices = (
	('male', 'Male'),
	('female', 'Female'),
)

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

Transfer_Type=(
	('Physical DIS','PhysicalDIS'),
	('Online eDIS','Online eDIS'),
	('NSDL Speed-e','CDSL Easi'),
	('CDSL Easi','CDSL Easi'),
	)
SignUp-Info=(
	('Individual','Individual'),
	('Solo Proprietorship Firm','Solo Proprietorship Firm'),
	('Partnership Firm','Partnership Firm'),
	('Private Limited Company','Private Limited Company'),
	('Public Limited Company','Public Limited Company'),
	)
Register-Info=(
	('SEBI-Stock Market','SEBI-Stock Market'),
	('AMFI-Mutual Funds','AMFI-Mutual Funds'),
	('IRDA-Insurance','IRDA-Insurance'),
	('None','None'),
	)

class channelPartnerPersonalDetails(models.Model):
	profileOwner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerCPPD',null=True,blank=True)
	name=models.CharField(max_length=1000,null=True,blank=True)
	email=models.EmailField(max_length=254,null=True,blank=True)
	mobileNumber=models.BigIntegerField(null=True,blank=True)
	gender=models.CharField(max_length=50,choices=Gender_Choices,null=True,blank=True)
	panCardNumber=models.CharField(max_length=100,null=True,blank=True)
	panCard=models.FileField(upload_to ='channelPartner/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	aadharCardNumber=models.BigIntegerField(null=,blank=True)
	aadharCard=models.FileField(upload_to='channelPartner/documents/',null=True,blank=True,validators=[FileExtensionValidator(['pdf'])])
	address=models.TextField(null=True,blank=True)
	city=models.ForeignKey(city,on_delete=models.SET_NULL,null=True,blank=True,related_name='cityCPPD')
	state=models.ForeignKey(state,on_delete=models.SET_NULL,null=True,blank=True,related_name='stateCPPD')
	country=models.ForeignKey(country,on_delete=models.SET_NULL,null=True,blank=True,related_name='countryCPPD')
	pinCode=models.BigIntegerField(null=True,blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorCPPD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Channel Partner Personal Detail'

class channelPartnerCompanyDetails(models.Model):
	pofileOwner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profileOwnerCPPD',null=True,blank=True)
	signUpAs=models.CharField(max_length=50,choices=SignUp-Info,null=True,blank=True)
	nameOfOrganization=models.CharField(max_length=1000,null=True,blank=True)
	companyAdress=models.TextField(null=True,blank=True)
	licence=models.CharField(max_length=50,null=True,blank=True)
	licenceProof=models.FileField(upload_to='channelPartner/documents/',null=True,blank=True,validators=[FileExtensionValidator['pdf']])
	city=models.ForeignKey(city,on_delete=SET_NULL,null=True,blank=True,related_name='cityCPCD')
	state=models.ForeignKey(state,on_delete=SET_NULL,null=True,blank=True,related_name='stateCPCD')
	country=models.ForeignKey(country,on_delete=SET_NULL,null=True,blank=True,related_name='countryCPCD')
	pincode=models.BigIntegerField(max_length=10,null=True,blank=True)
	companyWebsiteUrl=models.URLField(max_length=1000,null=True,blank=True)
	registerWith=models.CharField(max_length=100,null=True,blank=True,choices=Register-Info)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorCPCD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Channel Partner Company Details'




class channelPartnerBankDetails(models.Model):
	profileOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profileOwnerCPBD', null=True, blank=True)
	bankName = models.CharField(max_length=1000)
	accountHolder = models.CharField(max_length=1000, null=True, blank=True)
	accountNumber = models.BigIntegerField(null=True,blank=True)
	accountType=models.CharField(max_length=10,choices=AccountType_Info,null=True,blank=True)
	ifsc_Code = models.CharField(max_length=1000, null=True, blank=True)
	cancelledCheque = models.FileField(upload_to ='channelPartner/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorCPBD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.bankName or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Channel Partner Bank Detail'

class channelPartnerStockBrokerDetail(models.Model):
	name = models.CharField(max_length=1000, null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorCPSBD', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Channel Partner Stock Broker Detail'


class channnelPartnerDematInformation(models.Model):
	profileOwner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profileOwnerCPDI')
	stockBroker = models.ForeignKey('channelPartnerStockBrokerDetail', on_delete=models.SET_NULL, related_name="stockBrokerCPDI", null=True, blank=True)
	depository = models.CharField(max_length=10,choices=Depository_Info, null=True, blank=True)
	dmatClientMasterReport = models.FileField(upload_to ='channelPartner/documents/',null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
	dpID = models.CharField(max_length=1000, null=True, blank=True)
	clientID = models.BigIntegerField( null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorCPDI', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.dpID or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Channel Partner Demat Information'

class channelPartnerTransferFacilityDetail(models.Model):
	profileOwner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profileOwnerCPTFD', null=True, blank=True)
	transferShares=models.CharField(max_length=50, choices=Transfer_Type,null=True,blank=True)
	transferFileProof=models.FileField(upload_to='channelPartner/documents/',null=True,blank=True,validators=[FileExtensionValidator(['pdf'])])
	publish = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorCPTFD', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.transferShares or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Channel Partner Transfer Facility Detail'

class channelPartnerLinkedInModel(models.Model):
	profileOwner=models.OneToOneField(User,on_delete=models.SET_NULL,related_name='profileOwnerCPLIM',null=True,blank=True)
	profileOwnerMMM=models.ManyToManyField(User,on_delete=models.CASCADE,related_name='profileOwnerMMMCPLIM',blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorCPLIM', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.transferShares or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Channel Partner Linked In Model'
