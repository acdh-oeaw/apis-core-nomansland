# Generated by Django 3.1.14 on 2022-09-14 13:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apis_entities', '0004_auto_20220914_1336'),
        ('apis_vocabularies', '0002_expressionmanuscriptpartrelation_institutionmanuscriptpartrelation_manusciptparttype_manuscriptmanus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ManusciptpartType',
            new_name='ManuscriptpartType',
        ),
    ]