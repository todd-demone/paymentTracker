# Generated by Django 2.0.6 on 2018-06-26 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCardVendor', '0002_auto_20180626_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('^\\d{1,16}$')]),
        ),
        migrations.AlterField(
            model_name='card',
            name='security_code',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
