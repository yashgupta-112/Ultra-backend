# Generated by Django 3.2 on 2022-06-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0020_alter_tickets_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
