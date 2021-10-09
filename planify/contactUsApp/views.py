from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from .forms import *
from .models import *

def planifyEliteChannelPartnerView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		pkID = request.POST.get('dataID')
		if methodType == 'new':
			objlnst = None
		else:
			objlnst = get_object_or_404(planifyEliteChannelPartner, pk=pkID)
		objForm = planifyEliteChannelPartnerForm(request.POST, request.FILES, instance=objlnst)
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.save()
			cd.refresh_from_db()
			messages.success(request, 'Data sent for verification')
		else:
			messages.error(request, 'Please check An Error occurred')
		return redirect(redirectTo)
	return HttpResponse('Invalid Entry')
# Create your views here.
