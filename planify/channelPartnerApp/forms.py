from django import forms
from .models import *

class channelPartnerPersonalDetailsForm(forms.ModelForm):
	class Meta:
		model=channelPartnerPersonalDetails
		exclude=('profileOwner','author','publish','created','updated','status')

class channelPartnerBankDetailsForm(forms.ModelForm):
	class Meta:
		model=channelPartnerBankDetails
		exclude=('profileOwner','author','publish','created','updated','status')

class channelPartnerStockBrokerDetailForm(forms.ModelForm):
	class Meta:
		model=channelPartnerBankDetail
		exclude=('author','publish','created','updated','status')

class channnelPartnerDematInformationForm(forms.ModelForm):
	class Meta:
		model=channnelPartnerDematInformation
		exclude=('profileOwner','author','publish','created','updated','status')

class channelPartnerTransferFacilityDetailForm(forms.ModelForm):
	class Meta:
		model=channelPartnerTransferFacilityDetail
		exclude=('profileOwner','author','publish','created','updated','status')

class channelPartnerCompanyDetailsFrom(forms.ModelForm):
	class Meta:
		model=channelPartnerCompanyDetails
		exclude=('profileOwner','author','publish','created','updated','status')