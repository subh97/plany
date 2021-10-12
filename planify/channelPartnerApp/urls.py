from django.urls import path
from . import views

app_name='channelPartnerApp'

urlpatterns=[
    path('',views.homePageViews,name='homePageUrl'),
	path('personal-info', views.channelPartnerPersonalDetailsView, name='channelPartnerPersonalDetailsUrl'),
	path('bank-info',views.channelPartnerBankDetailsView,name='channelPartnerBankDetailsUrl'),
	path('company-info',views.channelPartnerCompanyDetailsView,name='channelPartnerCompanyDetailsUrl'),
	path('stockBroker-info',views.channelPartnerStockBrokerDetailView,name='channelPartnerStockBrokerDetailUrl'),
	path('demat-info',views.channnelPartnerDematInformationView,name='channnelPartnerDematInformationUrl'),
	path('transferFacility-info',views.channelPartnerTransferFacilityDetailView,name='channelPartnerTransferFacilityDetailUrl'),
]
