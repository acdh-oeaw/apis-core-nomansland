# Generated by Django 3.1.8 on 2022-06-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis_relations', '0005_workwork'),
        ('apis_entities', '0004_auto_20220426_1816'),
        ('apis_vocabularies', '0004_expressionpersonrelation'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkWorkRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.relationbaseclass')),
                ('workB_set', models.ManyToManyField(blank=True, related_name='workA_relationtype_set', through='apis_relations.WorkWork', to='apis_entities.Work')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_vocabularies.relationbaseclass',),
        ),
    ]
