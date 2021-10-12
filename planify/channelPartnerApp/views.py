from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from .forms import *
from .models import *


def homePageViews(request):
	return render(request,'channelPartner/homePage.html')


def channelPartnerPersonalDetailsView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(channelPartnerPersonalDetails, pk=pkID) 
		objForm =  channelPartnerPersonalDetailsForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')


def channelPartnerCompanyDetailsView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(channelPartnerCompanyDetails, pk=pkID) 
		objForm =  channelPartnerCompanyDetailsForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')


def channelPartnerBankDetailsView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(channelPartnerBankDetails, pk=pkID) 
		objForm =  channelPartnerBankDetailsForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')


def channelPartnerStockBrokerDetailView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(channelPartnerStockBrokerDetail, pk=pkID) 
		objForm =  channelPartnerStockBrokerDetailForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')



def channnelPartnerDematInformationView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(channnelPartnerDematInformation, pk=pkID) 
		objForm =  channnelPartnerDematInformationForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

def channelPartnerTransferFacilityDetailView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			objlnst = get_object_or_404(channelPartnerTransferFacilityDetail, pk=pkID) 
		objForm =  channelPartnerTransferFacilityDetailForm(request.POST, request.FILES, instance=objlnst) 
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')
