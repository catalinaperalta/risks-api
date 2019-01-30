from django.contrib import admin
from .models import Insurer, Risk, RiskField

admin.site.register(Insurer)
admin.site.register(Risk)
admin.site.register(RiskField)