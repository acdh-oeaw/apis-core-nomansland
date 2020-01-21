# Generated by Django 2.1.12 on 2020-01-21 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis_vocabularies', '0001_initial'),
        ('apis_entities', '0001_initial'),
        ('apis_relations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='event_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='work_set', through='apis_relations.EventWork', to='apis_vocabularies.EventWorkRelation'),
        ),
        migrations.AddField(
            model_name='work',
            name='institution_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='work_set', through='apis_relations.InstitutionWork', to='apis_vocabularies.InstitutionWorkRelation'),
        ),
        migrations.AddField(
            model_name='work',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.WorkType'),
        ),
        migrations.AddField(
            model_name='work',
            name='person_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='work_set', through='apis_relations.PersonWork', to='apis_vocabularies.PersonWorkRelation'),
        ),
        migrations.AddField(
            model_name='work',
            name='place_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='work_set', through='apis_relations.PlaceWork', to='apis_vocabularies.PlaceWorkRelation'),
        ),
        migrations.AddField(
            model_name='work',
            name='workB_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='workA_set', through='apis_relations.WorkWork', to='apis_vocabularies.WorkWorkRelation'),
        ),
        migrations.AddField(
            model_name='work',
            name='workB_set',
            field=models.ManyToManyField(blank=True, related_name='workA_set', through='apis_relations.WorkWork', to='apis_entities.Work'),
        ),
        migrations.AddField(
            model_name='place',
            name='event_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.PlaceEvent', to='apis_vocabularies.PlaceEventRelation'),
        ),
        migrations.AddField(
            model_name='place',
            name='event_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.PlaceEvent', to='apis_entities.Event'),
        ),
        migrations.AddField(
            model_name='place',
            name='institution_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.InstitutionPlace', to='apis_vocabularies.InstitutionPlaceRelation'),
        ),
        migrations.AddField(
            model_name='place',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.PlaceType'),
        ),
        migrations.AddField(
            model_name='place',
            name='person_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.PersonPlace', to='apis_vocabularies.PersonPlaceRelation'),
        ),
        migrations.AddField(
            model_name='place',
            name='placeB_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='placeA_set', through='apis_relations.PlacePlace', to='apis_vocabularies.PlacePlaceRelation'),
        ),
        migrations.AddField(
            model_name='place',
            name='placeB_set',
            field=models.ManyToManyField(blank=True, related_name='placeA_set', through='apis_relations.PlacePlace', to='apis_entities.Place'),
        ),
        migrations.AddField(
            model_name='place',
            name='work_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.PlaceWork', to='apis_vocabularies.PlaceWorkRelation'),
        ),
        migrations.AddField(
            model_name='place',
            name='work_set',
            field=models.ManyToManyField(blank=True, related_name='place_set', through='apis_relations.PlaceWork', to='apis_entities.Work'),
        ),
        migrations.AddField(
            model_name='person',
            name='event_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonEvent', to='apis_vocabularies.PersonEventRelation'),
        ),
        migrations.AddField(
            model_name='person',
            name='event_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonEvent', to='apis_entities.Event'),
        ),
        migrations.AddField(
            model_name='person',
            name='institution_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonInstitution', to='apis_vocabularies.PersonInstitutionRelation'),
        ),
        migrations.AddField(
            model_name='person',
            name='institution_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonInstitution', to='apis_entities.Institution'),
        ),
        migrations.AddField(
            model_name='person',
            name='personB_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='personA_set', through='apis_relations.PersonPerson', to='apis_vocabularies.PersonPersonRelation'),
        ),
        migrations.AddField(
            model_name='person',
            name='personB_set',
            field=models.ManyToManyField(blank=True, related_name='personA_set', through='apis_relations.PersonPerson', to='apis_entities.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='place_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonPlace', to='apis_vocabularies.PersonPlaceRelation'),
        ),
        migrations.AddField(
            model_name='person',
            name='place_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonPlace', to='apis_entities.Place'),
        ),
        migrations.AddField(
            model_name='person',
            name='profession',
            field=models.ManyToManyField(blank=True, to='apis_vocabularies.ProfessionType'),
        ),
        migrations.AddField(
            model_name='person',
            name='title',
            field=models.ManyToManyField(blank=True, to='apis_vocabularies.Title'),
        ),
        migrations.AddField(
            model_name='person',
            name='work_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonWork', to='apis_vocabularies.PersonWorkRelation'),
        ),
        migrations.AddField(
            model_name='person',
            name='work_set',
            field=models.ManyToManyField(blank=True, related_name='person_set', through='apis_relations.PersonWork', to='apis_entities.Work'),
        ),
        migrations.AddField(
            model_name='institution',
            name='event_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='institution_set', through='apis_relations.InstitutionEvent', to='apis_vocabularies.InstitutionEventRelation'),
        ),
        migrations.AddField(
            model_name='institution',
            name='event_set',
            field=models.ManyToManyField(blank=True, related_name='institution_set', through='apis_relations.InstitutionEvent', to='apis_entities.Event'),
        ),
        migrations.AddField(
            model_name='institution',
            name='institutionB_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='institutionA_set', through='apis_relations.InstitutionInstitution', to='apis_vocabularies.InstitutionInstitutionRelation'),
        ),
        migrations.AddField(
            model_name='institution',
            name='institutionB_set',
            field=models.ManyToManyField(blank=True, related_name='institutionA_set', through='apis_relations.InstitutionInstitution', to='apis_entities.Institution'),
        ),
        migrations.AddField(
            model_name='institution',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.InstitutionType'),
        ),
        migrations.AddField(
            model_name='institution',
            name='person_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='institution_set', through='apis_relations.PersonInstitution', to='apis_vocabularies.PersonInstitutionRelation'),
        ),
        migrations.AddField(
            model_name='institution',
            name='place_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='institution_set', through='apis_relations.InstitutionPlace', to='apis_vocabularies.InstitutionPlaceRelation'),
        ),
        migrations.AddField(
            model_name='institution',
            name='place_set',
            field=models.ManyToManyField(blank=True, related_name='institution_set', through='apis_relations.InstitutionPlace', to='apis_entities.Place'),
        ),
        migrations.AddField(
            model_name='institution',
            name='work_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='institution_set', through='apis_relations.InstitutionWork', to='apis_vocabularies.InstitutionWorkRelation'),
        ),
        migrations.AddField(
            model_name='institution',
            name='work_set',
            field=models.ManyToManyField(blank=True, related_name='institution_set', through='apis_relations.InstitutionWork', to='apis_entities.Work'),
        ),
        migrations.AddField(
            model_name='event',
            name='eventB_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='eventA_set', through='apis_relations.EventEvent', to='apis_vocabularies.EventEventRelation'),
        ),
        migrations.AddField(
            model_name='event',
            name='eventB_set',
            field=models.ManyToManyField(blank=True, related_name='eventA_set', through='apis_relations.EventEvent', to='apis_entities.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='institution_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='event_set', through='apis_relations.InstitutionEvent', to='apis_vocabularies.InstitutionEventRelation'),
        ),
        migrations.AddField(
            model_name='event',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='person_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='event_set', through='apis_relations.PersonEvent', to='apis_vocabularies.PersonEventRelation'),
        ),
        migrations.AddField(
            model_name='event',
            name='place_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='event_set', through='apis_relations.PlaceEvent', to='apis_vocabularies.PlaceEventRelation'),
        ),
        migrations.AddField(
            model_name='event',
            name='work_relationtype_set',
            field=models.ManyToManyField(blank=True, related_name='event_set', through='apis_relations.EventWork', to='apis_vocabularies.EventWorkRelation'),
        ),
        migrations.AddField(
            model_name='event',
            name='work_set',
            field=models.ManyToManyField(blank=True, related_name='event_set', through='apis_relations.EventWork', to='apis_entities.Work'),
        ),
    ]
