from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from .serializers import InsurerSerializer, RiskSerializer, RiskFieldSerializer
from .models import Insurer, Risk, RiskField

# Viewset for Insurer related views
class InsurerViewSet(viewsets.ModelViewSet):
	queryset = Insurer.objects.all()
	serializer_class = InsurerSerializer

# Viewset for the Risks model
class RiskViewSet(viewsets.ModelViewSet):
	queryset = Risk.objects.all()
	serializer_class = RiskSerializer

# Viewset for the Risk field model
class RiskFieldViewSet(viewsets.ModelViewSet):
	queryset = RiskField.objects.all()
	serializer_class = RiskFieldSerializer

	# Set filter_backends and search_fields in order to allow searching based on Risk field name and description
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'description')