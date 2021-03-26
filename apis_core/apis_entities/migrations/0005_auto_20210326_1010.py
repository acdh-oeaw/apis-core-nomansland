# Generated by Django 3.1.7 on 2021-03-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis_entities', '0004_auto_20200722_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="father's name"),
        ),
        migrations.AddField(
            model_name='person',
            name='grandfathers_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="grandfather's name"),
        ),
        migrations.AddField(
            model_name='person',
            name='laqab_kunya',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='laqab/kunya'),
        ),
    ]
