from django.contrib import admin

from ..models import ServiceOwnership


class ServiceOwnershipAdmin(admin.TabularInline):
    model = ServiceOwnership
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    inlines = [
        ServiceOwnershipAdmin,
    ]
