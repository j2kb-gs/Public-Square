from django.contrib import admin
from django.db import models

from apps.home.models import Borough, Hotspot_Borough, Hotspot_Location, Hotspot_Neighborhood, Hotspot_Provider, Neighborhood, Provider

# Register your models here.
admin.site.register(Hotspot_Location)
admin.site.register(Provider)
admin.site.register(Hotspot_Provider)
admin.site.register(Borough)
admin.site.register(Hotspot_Borough)
admin.site.register(Neighborhood)
admin.site.register(Hotspot_Neighborhood)