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

@admin.register(institutionalPersonalDetails) 
class institutionalPersonalDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]
# Company Admin
@admin.register(registerWithSEBIDetails) 
class registerWithSEBIDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(institutionalCompanyDetails) 
class institutionalCompanyDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

# investment Admin

@admin.register(lookingForPrivateCompany) 
class lookingForPrivateCompanyImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(lookingToInvestDetails) 
class lookingToInvestDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(majorSectorDetails) 
class majorSectorDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]


@admin.register(institutionalInvestmentDetails) 
class institutionalInvestmentDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

#bank Admin
@admin.register(institutionalBankDetails) 
class institutionalBankDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

#Demat admin
@admin.register(stockBrokerDetails) 
class stockBrokerDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(institutionalDematDetails) 
class institutionalDematDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

#transfer Facility Admin
@admin.register(transferFacilityDetails) 
class transferFacilityDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]


