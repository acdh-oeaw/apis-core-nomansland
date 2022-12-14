# Generated by Django 3.1.8 on 2022-06-10 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis_metainfo', '0002_auto_20220408_1654'),
        ('apis_vocabularies', '0006_placeexpressionrelation'),
        ('apis_entities', '0005_auto_20220610_1248'),
        ('apis_relations', '0006_workwork_relation_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceExpression',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.tempentityclass')),
                ('certainty', models.CharField(blank=True, choices=[(None, '---'), ('low', 'low'), ('medium', 'medium'), ('high', 'high')], help_text='Specify the certainty of this information.', max_length=10, null=True)),
                ('related_expression', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placeexpression_set', to='apis_entities.expression')),
                ('related_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placeexpression_set', to='apis_entities.place')),
                ('relation_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placeexpression_set', to='apis_vocabularies.placeexpressionrelation')),
            ],
            options={
                'abstract': False,
                'default_manager_name': 'objects',
            },
            bases=('apis_metainfo.tempentityclass',),
        ),
    ]
