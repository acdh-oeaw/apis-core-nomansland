# Generated by Django 3.1.8 on 2022-04-25 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis_vocabularies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectsAnnotations',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.vocabsbaseclass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
    ]
