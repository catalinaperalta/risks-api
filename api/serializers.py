from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Insurer, Risk, RiskField

class RiskFieldSerializer(serializers.ModelSerializer):
    # risk = RiskSerializer(read_only=True)

    class Meta:
        model = RiskField
        fields = ('id', 'name', 'description', 'value', 'field_type', 'risk')

class RiskSerializer(serializers.ModelSerializer):
    # Operation to reverse the relationship in many to one models so that the api can return a risk type with all of its related risk fields
    risk_fields = RiskFieldSerializer(many=True, required=False)

    class Meta:
        model = Risk
        fields = ('id', 'name', 'description', 'coverage_amount', 'risk_fields')

class InsurerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurer
        fields = ('id', 'url', 'name', 'description', 'year_founded', 'industry')