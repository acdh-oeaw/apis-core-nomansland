# Generated by Django 3.1.8 on 2022-04-26 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis_vocabularies', '0003_scripttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressionPersonRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.relationbaseclass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_vocabularies.relationbaseclass',),
        ),
    ]
