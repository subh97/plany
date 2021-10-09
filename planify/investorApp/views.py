from django.shortcuts import render, get_object_or_404, redirect, HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm

#Form Submitted#
"""if request.method == 'POST':
		form = signUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect('accounts:profile')
	else:
		form = signUpForm()
	return render(request, 'investor/homePage.html', {'form': form})"""
def homePageViews(request):
	
    if request.method=='POST':
        form=signUpForm(request.POST)
        if form.is_valid():
        	email=form.cleaned_data.get('email')
        	try:
        		match = User.objects.get(email=email)
        	except User.DoesNotExist:
        		return email
        	raise forms.ValidationError('This email address is already in use.')   
        	messages.success(request,'Account Created Successfully')
        	form.save()
    else:
        form=signUpForm()
    return render(request,'investor/homePage.html',{'form':form})


def loginView(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/investor/personalDetail/')

    else:
        form=AuthenticationForm()
    return render(request,'investor/loginPage.html',{'form':form})

def investorHomePage(request):
	return render(request,'investor/personalDetail.html')
	

def investorPersonalDetailsView(request):
	if request.method == 'POST':
		methodType = request.POST.get('submitType')
		redirectTo = request.POST.get('requestFrom')
		redirectSuccess = request.POST.get('redirecting')
		if methodType == 'new':
			objlnst = None
		else:
			pkID = request.POST.get('dataID')
			# shubham start
			objlnst = get_object_or_404(investorPersonalDetails, pk=pkID)  #change model name
		objForm =  investorPersonalDetailsForm(request.POST, request.FILES, instance=objlnst) #change form name
		#shubham ends
		if objForm.is_valid():
			cd = objForm.save(commit=False)
			cd.createdBy = request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

# start writing code by shubham
def investmentDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')

			objlnst=get_object_or_404(investmentDetails,pk=pkID)
		objForm=investmentDetailsForm(request.POST,request.FILES,instance=objlnst)

		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')
	

def investorBankDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')

			objlnst=get_object_or_404(investorBankDetails,pk=pkID)
		objForm=investorBankDetailsForm(request.POST,request.FILES,instance=objlnst)

		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

def investorDMATDetailsView(request):

	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.POST.get('dataID')

			objlnst=get_object_or_404(investorDMATDetails,pk=pkID)
		objForm=investorDMATDetailsForm(request.POST,request.FILES,instance=objlnst)

		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
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
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')

def lookingToInvestDetailsView(request):
	if request.method=='POST':
		methodType=request.POST.get('submitType')
		redirectTo=request.POST.get('requestFrom')
		redirectSuccess=request.POST.get('redirecting')
		if methodType=='new':
			objlnst=None
		else:
			pkID=request.post.get('dataID')
			objlnst=get_object_or_404(lookingToInvestDetails,pk=pkID)
		objForm=lookingToInvestDetailsForm(request.POST,request.FILES,instance=objlnst)
		if objForm.is_valid():
			cd=objForm.save(commit=False)
			cd.createdBy=request.user
			cd.save()
			cd.refresh_from_db()
			return JsonResponse({'error': False, 'message': 'Updated Successfully'})	
		else:
			return JsonResponse({'error': True, 'errors': objForm.errors})
	return HttpResponse('Invalid Entry')
# ends the code by shuham


""" SignUp Views """

#def signUpView(request):
	


 
