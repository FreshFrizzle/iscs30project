# Generated by Django 3.2 on 2023-05-15 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_alter_forumpost_pub_datetime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forumpost',
            options={'ordering': ('-pub_datetime',)},
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='pub_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 12, 5, 8, 946005)),
        ),
    ]
