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

@admin.register(planifyEliteChannelPartner) 
class planifyEliteChannelPartnerImport(ImportExportModelAdmin):
	actions = [approvePost, draftPost,]
