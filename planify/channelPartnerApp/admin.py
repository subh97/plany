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
draftPost.short_description = 'Draft Selected'

@admin.register(channelPartnerPersonalDetails) 
class channelPartnerPersonalDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]


@admin.register(channelPartnerBankDetails) 
class channelPartnerBankDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(channelPartnerStockBrokerDetail) 
class channelPartnerStockBrokerDetailImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(channnelPartnerDematInformation) 
class channnelPartnerDematInformationImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(channelPartnerTransferFacilityDetail) 
class channelPartnerTransferFacilityDetailImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(channelPartnerCompanyDetails)
class channelPartnerCompanyDetailsImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost,]

