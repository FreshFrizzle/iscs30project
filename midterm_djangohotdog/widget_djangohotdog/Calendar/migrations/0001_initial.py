# Generated by Django 4.1.6 on 2023-03-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_datetime', models.CharField(max_length=100)),
                ('activity', models.CharField(max_length=100)),
                ('estimated_hours', models.FloatField(default='0')),
                ('location', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=6)),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
    ]
