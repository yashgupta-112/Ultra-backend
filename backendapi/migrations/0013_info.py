# Generated by Django 3.2 on 2022-06-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0012_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waiting', models.IntegerField(default=1)),
                ('news', models.CharField(max_length=150)),
                ('reply', models.IntegerField(default=30)),
            ],
        ),
    ]
