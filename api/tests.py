from django.urls import reverse
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import Risk, RiskField, Insurer

# Test suite for Risk Model
class RiskTests(APITestCase):
	# TEST: check if risks can be created correctly and saved
	def test_risk_creation(self):
		float_num = Risk(name="Risk A", description="Description for Risk A", coverage_amount=25000.00)
		float_num.full_clean()
		float_num.save()
		self.assertIs(isinstance(float_num, Risk), True)
		self.assertEqual(Risk.objects.count(), 1)


	# TEST: check if validation does prevent Risks from being saved with negative coverage amounts
	def test_risk_creation_neg_coverage(self):
		neg_num = Risk(name="Risk A", description="Description for Risk A", coverage_amount=-1)

		try:
			neg_num.full_clean()
		except ValidationError as e:
			self.assertTrue('coverage_amount' in e.message_dict)

	# TEST: check if the risks api endpoint does return the right information
	def test_risk_endpoint(self):
		response = self.client.get('/api/risks/')
		self.assertTrue(status.is_success(response.status_code))

# Test suite for the Risk Field Model
class RiskFieldTests(APITestCase):
	# TEST: check if risk fields can be created correctly and saved
	def test_riskfield_creation(self):
		risk_a = Risk(name="Risk A", description="Description of Risk A", coverage_amount = 10)
		risk_a.full_clean()
		risk_a.save()
		riskfield = RiskField(name="RiskField A", description="Description for RiskField A", value="25", field_type="NUMBER", risk = Risk(id=1))
		riskfield.full_clean()
		riskfield.save()
		self.assertIs(isinstance(riskfield, RiskField), True)
		self.assertEqual(RiskField.objects.count(), 1)

	# TEST: check if risk fields can be saved without a related Risk
	def test_riskfield_creation_without_risk(self):
		riskfield = RiskField(name="RiskField A", description="Description for RiskField A", value="25", field_type="NUMBER")
		
		try:
			riskfield.full_clean()
		except ValidationError as e:
			self.assertTrue('risk' in e.message_dict)

	# TEST: check if the risk field api endpoint does return the right information
	def test_riskfields_endpoint(self):
		response = self.client.get('/api/riskfields/')
		self.assertTrue(status.is_success(response.status_code))

	# TEST: check if the risk field api endpoint does return the right information when just searching for one particular Risk field
	def test_riskfield_endpoint(self):
		risk_a = Risk(name="Risk A", description="Description of Risk A", coverage_amount = 10)
		risk_a.full_clean()
		risk_a.save()
		riskfield = RiskField(name="RiskField A", description="Description for RiskField A", value="25", field_type="NUMBER", risk = Risk(id=1))
		riskfield.full_clean()
		riskfield.save()
		response = self.client.get('/api/riskfields/?search=RiskField A')
		self.assertTrue(status.is_success(response.status_code))