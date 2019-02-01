from django.db import models
from django.core.validators import MinValueValidator

# Risk model used to hold information about risks insurers will cover. In FUTURE each risk needs to be linked to a particular insurer. 
class Risk(models.Model):
	name = models.CharField(max_length=100)
	# Field to descript the type of risk that will be covered
	description = models.CharField(max_length=256)
	# Field that will be used to determine the maximum coverage amount allowed for that particular risk type
	coverage_amount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

	class Meta:
		ordering = ('name',)
		verbose_name = "risk"

# Risk field model is used to add as many additional fields needed for each risk. Each risk field is linked to one Risk type. 
class RiskField(models.Model):
	name = models.CharField(max_length=100)
	# Description of the purpose of a particular risk field
	description = models.CharField(max_length=256)
	# Value will hold the actual value for that particular Risk Field. 
	value = models.CharField(max_length=256) 

	# The only permissable options for the field_type field
	FIELD_CHOICES = (
		('TEXT', 'TEXT'),
		('NUMBER', 'NUMBER'),
		('DATE', 'DATE'),
		('ENUM', 'ENUM'))

	field_type = models.CharField(
		max_length=40,
		choices=FIELD_CHOICES,
		default='TEXT')

	# Foreign Key related to the Risk type that this Risk field will belong to
	risk = models.ForeignKey(Risk, related_name='risk_fields', on_delete=models.CASCADE)

	class Meta:
		ordering = ('name',)
		verbose_name = "riskfield"

	def __unicode__(self):
		return '%s: %s' % (self.name, self.description)

# Insurer class that will be used in the future to relate each insurer to their risks
class Insurer(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=256)
	year_founded = models.IntegerField()
	industry = models.CharField(max_length=80)
	url = models.CharField(max_length=256)

	class Meta:
		ordering = ('name',)
		verbose_name = "insurer"