# Generated by Django 2.1.5 on 2019-01-29 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=256)),
                ('coverage_amount', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
                ('field_type', models.CharField(choices=[('TEXT', 'TEXT'), ('NUMBER', 'NUMBER'), ('DATE', 'DATE'), ('ENUM', 'ENUM')], default='TEXT', max_length=40)),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Risk')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='insurer',
            options={'ordering': ('name',)},
        ),
    ]
