# Generated by Django 3.2 on 2022-05-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0002_rename_essential_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='price',
            field=models.FloatField(),
        ),
    ]
