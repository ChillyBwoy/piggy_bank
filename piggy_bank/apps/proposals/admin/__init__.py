from django.contrib import admin

from ..models import Service

from .service import ServiceAdmin

admin.site.register(Service, ServiceAdmin)
