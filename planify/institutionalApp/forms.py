from django import forms
from .models import *
# personal Forms
class institutionalPersonalDetailsForm(forms.ModelForm):
	class Meta:
		model=institutionalPersonalDetails
		exclude=('profileOwner','author','publish','created','updated','status')

#company Forms
class registerWithSEBIDetailsForm(forms.ModelForm):
	class Meta:
		model=registerWithSEBIDetails
		exclude=('author','publish','created','updated','status')


class institutionalCompanyDetailsForm(forms.ModelForm):
	class Meta:
		model=institutionalCompanyDetails
		exclude=('profileOwner','author','publish','created','updated','status')
#investment details Forms

class lookingToInvestDetailsForm(forms.ModelForm):
	class Meta:
		model=lookingToInvestDetails
		exclude=('author','publish','created','updated','status')

class lookingForPrivateCompanyForm(forms.ModelForm):
	class Meta:
		model=lookingForPrivateCompany
		exclude=('author','publish','created','updated','status')

class majorSectorDetailsForm(forms.ModelForm):
	class Meta:
		model=majorSectorDetails
		exclude=('author','publish','created','updated','status')


class institutionalInvestmentDetailsForm(forms.ModelForm):
	class Meta:
		model=institutionalInvestmentDetails
		exclude=('profileOwner','author','publish','created','updated','status')

# institutional bank detail model
class institutionalBankDetailsForm(forms.ModelForm):
	class Meta:
		model=institutionalBankDetails
		exclude=('profileOwner','author','publish','created','updated','status')

# Demat detail Forms

class stockBrokerDetailsForm(forms.ModelForm):
	class Meta:
		model=stockBrokerDetails
		exclude=('author','publish','created','updated','status')

class institutionalDematDetailsForm(forms.ModelForm):
	class Meta:
		model=institutionalDematDetails
		exclude=('profileOwner','author','publish','created','updated','status')


class transferFacilityDetailsForm(forms.ModelForm):
	class Meta:
		model=transferFacilityDetails
		exclude=('profileOwner','author','publish','created','updated','status')
