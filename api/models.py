from django.db import models
from django.core.validators import MinValueValidator

class Risk(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=256)
	coverage_amount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

	class Meta:
		ordering = ('name',)
		verbose_name = "risk"

class RiskField(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=256)
	value = models.CharField(max_length=256) 

	FIELD_CHOICES = (
		('TEXT', 'TEXT'),
		('NUMBER', 'NUMBER'),
		('DATE', 'DATE'),
		('ENUM', 'ENUM'))

	field_type = models.CharField(
		max_length=40,
		choices=FIELD_CHOICES,
		default='TEXT')

	risk = models.ForeignKey(Risk, related_name='risk_fields', on_delete=models.CASCADE)

	class Meta:
		ordering = ('name',)
		verbose_name = "riskfield"

	def __unicode__(self):
		return '%s: %s' % (self.name, self.description)

class Insurer(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=256)
	year_founded = models.IntegerField()
	industry = models.CharField(max_length=80)
	url = models.CharField(max_length=256)

	class Meta:
		ordering = ('name',)
		verbose_name = "insurer"