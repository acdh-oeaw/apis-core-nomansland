# Generated by Django 3.1.8 on 2022-06-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis_vocabularies', '0006_placeexpressionrelation'),
        ('apis_relations', '0007_placeexpression'),
        ('apis_entities', '0005_auto_20220610_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='expression',
            name='place_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='expression_set', through='apis_relations.PlaceExpression', to='apis_vocabularies.PlaceExpressionRelation'),
        ),
        migrations.AddField(
            model_name='place',
            name='expression_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.PlaceExpression', to='apis_vocabularies.PlaceExpressionRelation'),
        ),
        migrations.AddField(
            model_name='place',
            name='expression_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.PlaceExpression', to='apis_entities.Expression'),
        ),
    ]
