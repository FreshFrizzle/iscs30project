# Generated by Django 4.1.6 on 2023-03-05 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='activity',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Calendar.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='mode',
            field=models.TextField(max_length=6),
        ),
        migrations.AlterField(
            model_name='location',
            name='venue',
            field=models.TextField(max_length=200),
        ),
    ]
