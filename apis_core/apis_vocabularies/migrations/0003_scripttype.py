# Generated by Django 3.1.8 on 2022-04-26 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis_vocabularies', '0002_subjectsannotations'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.vocabsbaseclass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
    ]
