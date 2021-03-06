# Generated by Django 3.2 on 2022-05-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='essential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('storage', models.CharField(max_length=255)),
                ('traffic', models.CharField(max_length=255)),
                ('media', models.BooleanField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
