# Generated by Django 4.1.6 on 2023-03-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement_board', '0002_auto_20230305_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='name',
            field=models.CharField(blank=True, choices=[('Like', 'Like'), ('Love', 'Love'), ('Angry', 'Angry')], max_length=5),
        ),
    ]