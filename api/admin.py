from django.contrib import admin
from .models import Insurer, Risk, RiskField

# Registered models to facilitate modification through the admin portal
admin.site.register(Insurer)
admin.site.register(Risk)
admin.site.register(RiskField)