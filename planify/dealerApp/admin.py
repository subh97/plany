from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

def approvePost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Published'
		post.save()
approvePost.short_description = 'Approve Selected'


def draftPost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Draft'
		post.save()
# draftPost.short_description = 'Draft Selected'

@admin.register(dealersNetworkDetails) 
class dealersNetworkDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(dealerPersonalDetail) 
class dealerPersonalDetailImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(registerWithSEBIDetail)
class registerWithSEBIDetailImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]

@admin.register(dealerCompanyDetail)
class dealerCompanyDetailImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]

@admin.register(dealerBankDetail)
class dealerBankDetailImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]

@admin.register(stockBrokerDetail)
class stockBrokerDetailImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]

@admin.register(dealerDematDetail)
class dealerDematDetailImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]

@admin.register(dealerTransferFacilityDetail)
class dealerTransferFacilityDetailImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]

@admin.register(linkedInModels)
class linkedInModelsImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]