from django.urls import path
from . import views

app_name = 'investorApp'

urlpatterns = [
	#path('', views.employeeListView, name="employeeListUrl"),
	path('',views.homePageViews,name='homePageUrl'),
	path('login',views.loginView,name='loginUrl'),
	path('personalDetail/',views.investorHomePage,name='investorHomePage'),
	path('personal-info', views.investorPersonalDetailsView, name='investorPersonalDetailsUrl'),
	path('investment-info',views.investmentDetailsView, name='investmentDetailsUrl'),
	path('bank-info',views.investorBankDetailsView, name='investorBankDetailsUrl'),
	path('DMAT-info',views.investorDMATDetailsView, name='investorDMATDetailsUrl'),
	path('invest-info',views.lookingToInvestDetailsView,name='investmentINDetailsUrl')

]