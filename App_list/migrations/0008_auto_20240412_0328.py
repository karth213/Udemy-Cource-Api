# Generated by Django 3.2.10 on 2024-04-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_list', '0007_auto_20240412_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='Avg_rating',
            new_name='avg_rating',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='Ratting',
            field=models.IntegerField(),
        ),
    ]
