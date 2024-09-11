from django.contrib import admin
from .models import *

@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('pk','name')

@admin.register(Plan)
class AdminPlan(admin.ModelAdmin):
    list_display = ('pk','plan_type')

@admin.register(Subscription)
class AdminSubscription(admin.ModelAdmin):
    list_display = ('pk','client','plan','service')
