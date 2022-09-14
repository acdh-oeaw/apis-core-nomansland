# Generated by Django 3.1.14 on 2022-09-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, help_text='The entities label or name.', max_length=255)),
                ('arabic_script', models.CharField(blank=True, help_text='Label in arabic script if needed', max_length=255, null=True)),
                ('isoCode_639_3', models.CharField(blank=True, default='deu', help_text="The ISO 639-3 (or 2) code for the label's language.", max_length=3, null=True, verbose_name='ISO Code')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('start_start_date', models.DateField(blank=True, null=True)),
                ('start_end_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_start_date', models.DateField(blank=True, null=True)),
                ('end_end_date', models.DateField(blank=True, null=True)),
                ('start_date_written', models.CharField(blank=True, max_length=255, null=True, verbose_name='Start')),
                ('end_date_written', models.CharField(blank=True, max_length=255, null=True, verbose_name='End')),
            ],
        ),
    ]
