# Generated by Django 3.2.6 on 2021-12-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0003_auto_20211201_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='address_x',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='workshop',
            name='address_y',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
