from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#code need to be  add by Shubham starts

class planifyEliteChannelPartnerForm(forms.ModelForm):
	class Meta:
		model = planifyEliteChannelPartner
		exclude = ('author','publish','created','updated','status')