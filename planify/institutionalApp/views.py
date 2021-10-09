from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from .forms import *
from .models import *


def homePageViews(request):
	return render(request,'institutional/homePage.html')


def institutionalPersonalDetailsView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(institutionalPersonalDetails, pk=pkID) 
		objForm =  institutionalPersonalDetailsForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

#comany Dtails
def registerWithSEBIDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(registerWithSEBIDetails,pk=pkID)
		objForm=registerWithSEBIDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')



def institutionalCompanyDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestForm')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlst=None
		else:
			pkID=request.POST.get('dataID')
			objlst=get_object_or_404(institutionalCompanyDetails,pk=pkID)
		objForm=institutionalCompanyDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')

"""  investment Detail view """
def lookingForPrivateCompanyView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(lookingForPrivateCompany,pk=pkID)
		objForm=lookingForPrivateCompanyForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')


def lookingToInvestDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(lookingToInvestDetails,pk=pkID)
		objForm=lookingToInvestDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')

def majorSectorDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(majorSectorDetails,pk=pkID)
		objForm=majorSectorDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')


def institutionalInvestmentDetailsViews(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(institutionalInvestmentDetails,pk=pkID)
		objForm=institutionalInvestmentDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')

""" bank details View """

def institutionalBankDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(institutionalBankDetails,pk=pkID)
		objForm=institutionalBankDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')


def stockBrokerDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(stockBrokerDetails,pk=pkID)
		objForm=stockBrokerDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')

def institutionalDematDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(institutionalDematDetails,pk=pkID)
		objForm=institutionalDematDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')


def transferFacilityDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(transferFacilityDetails,pk=pkID)
		objForm=transferFacilityDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False,'message':'Updated Successfully'})
		else:
			return JsonResponse({'error':True,'errors':objForm.errors})
	return HttpResponse('Invalid Entry')