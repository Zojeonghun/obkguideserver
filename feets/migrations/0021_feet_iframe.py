# Generated by Django 3.2.6 on 2022-01-24 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feets', '0020_auto_20220124_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='feet',
            name='iframe',
            field=models.TextField(blank=True),
        ),
    ]
