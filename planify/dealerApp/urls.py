from django.urls import path
from . import views

app_name = 'dealerApp'
urlpatterns = [
    
    path('',views.homePageViews,name='homePageUrl'),
	path('network-info', views.dealersNetworkDetailsView, name='dealersNetworkDetailsUrl'),
	path('personal-info', views.dealerPersonalDetailView, name='dealerPersonalDetailUrl'),
	path('company-info',views.dealerCompanyDetailView, name='dealerCompanyDetailUrl'),
	path('bank-info',views.dealerBankDetailView, name='dealerBankDetailUrl'),
	path('SEBI-info',views.registerWithSEBIDetailView, name='registerWithSEBIDetailView'),

	path('Demat-info',views.dealerDematDetailView, name='dealerDematDetailUrl'),
	path('stock-info',views.stockBrokerDetailView,name='stockBrokerDetailUrl'),
	path('transfer-info',views.dealerTransferFacilityDetailView,name='dealerTransferFacilityDetailUrl'),


]




