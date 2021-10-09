from django.urls import path
from . import views

app_name = 'institutionalApp'
urlpatterns = [
    
    path('',views.homePageViews,name='homePageUrl'),
	path('personal-info', views.institutionalPersonalDetailsView, name='institutionalPersonalDetailsUrl'),
	path('registerSEBI-info', views.registerWithSEBIDetailsView, name='registerWithSEBIDetailsUrl'),
	path('company-info',views.institutionalCompanyDetailsView, name='institutionalCompanyDetailsUrl'),
	path('privateCompany-info',views.lookingForPrivateCompanyView, name='lookingForPrivateCompanyUrl'),
	path('invest-info',views.lookingToInvestDetailsView, name='lookingToInvestDetailsUrl'),
	path('majorSector-info',views.majorSectorDetailsView, name='majorSectorDetailsViewUrl'),
	path('investment-info',views.institutionalInvestmentDetailsViews, name='institutionalInvestmentDetailsUrl'),

	path('bank-info',views.institutionalBankDetailsView, name='institutionalBankDetailsUrl'),
	path('Demat-info',views.institutionalDematDetailsView, name='institutionalDematDetailsUrl'),
	path('stock-info',views.stockBrokerDetailsView,name='stockBrokerDetailsViewUrl'),
	path('transfer-info',views.transferFacilityDetailsView,name='transferFacilityDetailsUrl'),


]




