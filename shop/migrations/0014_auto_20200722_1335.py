# Generated by Django 3.0.7 on 2020-07-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200722_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
