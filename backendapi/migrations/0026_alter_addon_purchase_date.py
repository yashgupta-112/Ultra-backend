# Generated by Django 3.2 on 2022-06-06 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0025_alter_addon_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addon',
            name='purchase_date',
            field=models.DateField(default=datetime.date(2022, 6, 6)),
        ),
    ]
