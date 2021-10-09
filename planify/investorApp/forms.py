from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#code need to be  add by Shubham starts

class investorPersonalDetailsForm(forms.ModelForm):
	class Meta:
		model = investorPersonalDetails
		exclude = ('profileOwner','author','publish','created','updated','status')

class investmentDetailsForm(forms.ModelForm):
	class Meta:
		model = investmentDetails
		exclude = ('profileOwner','author','publish','created','updated','status')

class investorBankDetailsForm(forms.ModelForm):
	class Meta:
		model=investorBankDetails
		exclude=('profileOwnerFK','author','publish','created','updated','status')

class investorDMATDetailsForm(forms.ModelForm):
	class Meta:
		model=investorDMATDetails
		exclude=('profileOwner','author','publish','created','updated','status')


class stockBrokerDetailsForm(forms.ModelForm):
	class Meta:
		model=stockBrokerDetails
		exclude=('author','publish','created','updated','status')
		
class lookingToInvestDetailsForm(forms.ModelForm):
	class Meta:
		model=lookingToInvestDetails
		exclude=('author','publish','created','updated','status')



""" SignUp Form """
class signUpForm(UserCreationForm):


	class Meta:
		model=User
		fields=('username','email')
		labels={'email':'Email'}

	#def clean_email(self):
	#	email = self.cleaned_data.get('email')
	#	try:
	#		match = User.objects.get(email=email)def clean_email(self):
		#email = self.cleaned_data['email']
		#if self.Meta.model.objects.filter(email=email).exists():
		#	raise forms.ValidationError('Looks like email already exists')
		#return email
	#	except User.DoesNotExist:
	#		return email
	#	raise forms.ValidationError('This email address is already in use.')













	#email=forms.EmailField(required=True)
	#class Meta:
		#model=User
		#fields=['username','email','password1','password2']
		#labels={'email':'Email'}
	#def save(self,commit=True):
	#	user=super(signUpForm,self).save(commit=False)
	#	user.email=self.cleaned_data['email']
	#	if commit:
	#		user.save()
	#	return user





