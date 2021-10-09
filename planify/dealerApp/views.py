from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from .forms import *
from .models import *


def homePageViews(request):
	return render(request,'dealer/homePage.html')


def dealersNetworkDetailsView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(dealersNetworkDetails, pk=pkID) 
		objForm =  dealersNetworkDetailsForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

def dealerPersonalDetailView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(dealerPersonalDetail,pk=pkID)
		objForm=dealerPersonalDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')


def registerWithSEBIDetailView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(registerWithSEBIDetail,pk=pkID)
		objForm=registerWithSEBIDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

def dealerCompanyDetailView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(dealerCompanyDetail,pk=pkID)
		objForm=dealerCompanyDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')



def dealerBankDetailView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(dealerBankDetail,pk=pkID)
		objForm=dealerBankDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')




def stockBrokerDetailView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(stockBrokerDetail,pk=pkID)
		objForm=stockBrokerDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')


def dealerDematDetailView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(dealerDematDetail,pk=pkID)
		objForm=dealerDematDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

def dealerTransferFacilityDetailView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')
			objlnst=get_object_or_404(dealerTransferFacilityDetail,pk=pkID)
		objForm=dealerTransferFacilityDetailForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

