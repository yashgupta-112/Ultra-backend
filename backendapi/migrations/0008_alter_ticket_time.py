# Generated by Django 3.2 on 2022-06-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0007_ticket_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]