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

# Added By shubham starts

@admin.register(investorPersonalDetails) 
class investorPersonalDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(investmentDetails) 
class investmentDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(investorBankDetails) 
class investorBankDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(investorDMATDetails) 
class investorDMATDetailsImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]

@admin.register(stockBrokerDetails)
class stockBrokerDetailsImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost]

@admin.register(lookingToInvestDetails)
class lookingToInvestDetailsImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost]

@admin.register(linkedInModel)
class linkedInModelImport(ImportExportModelAdmin):
	actions=[approvePost,draftPost]
#shubham ends


