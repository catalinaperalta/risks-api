# Generated by Django 2.1.5 on 2019-01-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190129_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='coverage_amount',
            field=models.IntegerField(),
        ),
    ]
