# Generated by Django 3.2 on 2022-06-05 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0016_alter_tickets_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]