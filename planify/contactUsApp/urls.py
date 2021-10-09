from django.urls import path
from . import views

app_name = 'contactUsApp'

urlpatterns = [
	#path('', views.employeeListView, name="employeeListUrl"),
	path('EliteChannelPartner-info',views.planifyEliteChannelPartnerView,name='planifyEliteChannelPartnerURL')

]