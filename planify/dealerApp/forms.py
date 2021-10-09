from django import forms
from .models import *

class dealersNetworkDetailsForm(forms.ModelForm):
	class Meta:
		model=dealersNetworkDetails
		exclude=('profileOwner','author','publish','created','updated','status')

class dealerPersonalDetailForm(forms.ModelForm):
	class Meta:
		model=dealerPersonalDetail
		exclude=('profileOwner','author','publish','created','updated','status')

class registerWithSEBIDetailForm(forms.ModelForm):
	class Meta:
		model=registerWithSEBIDetail
		exclude=('author','publish','created','updated','status')

class dealerCompanyDetailForm(forms.ModelForm):
	class Meta:
		model=dealerCompanyDetail
		exclude=('profileOwner','author','publish','created','updated','status')


class dealerBankDetailForm(forms.ModelForm):
	class Meta:
		model=dealerBankDetail
		exclude=('profileOwner','author','publish','created','updated','status')

class stockBrokerDetailForm(forms.ModelForm):
	class Meta:
		model=stockBrokerDetail
		exclude=('author','publish','created','updated','status')


class dealerDematDetailForm(forms.ModelForm):
	class Meta:
		model=dealerDematDetail
		exclude=('profileOwner','author','publish','created','updated','status')

class dealerTransferFacilityDetailForm(forms.ModelForm):
	class Meta:
		model=dealerTransferFacilityDetail
		exclude=('profileOwner','author','publish','created','updated','status')