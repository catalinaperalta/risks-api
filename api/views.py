from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from .serializers import InsurerSerializer, RiskSerializer, RiskFieldSerializer
from .models import Insurer, Risk, RiskField

class InsurerViewSet(viewsets.ModelViewSet):
	queryset = Insurer.objects.all()
	serializer_class = InsurerSerializer

class RiskViewSet(viewsets.ModelViewSet):
	queryset = Risk.objects.all()
	serializer_class = RiskSerializer

class RiskFieldViewSet(viewsets.ModelViewSet):
	queryset = RiskField.objects.all()
	serializer_class = RiskFieldSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'description')