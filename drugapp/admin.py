from django.contrib import admin

from django.contrib import admin
from .models import Complaint,Alerts,CriminalDetails,Coma

admin.site.register(Complaint)
admin.site.register(Alerts)
admin.site.register(CriminalDetails)
admin.site.register(Coma)

