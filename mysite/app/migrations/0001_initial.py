# Generated by Django 3.1.3 on 2020-11-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScientificNames',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_code', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('name_code_sp2k', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('genus', models.CharField(blank=True, max_length=80, null=True)),
                ('species', models.CharField(blank=True, max_length=100, null=True)),
                ('infraspecies_marker', models.CharField(blank=True, max_length=20, null=True)),
                ('infraspecies', models.CharField(blank=True, max_length=50, null=True)),
                ('infraspecies2_marker', models.CharField(blank=True, max_length=20, null=True)),
                ('infraspecies2', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
                ('author2', models.CharField(blank=True, max_length=150, null=True)),
                ('accepted_name_code', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('datelastmodified', models.DateField(blank=True, null=True)),
                ('status_id', models.IntegerField(blank=True, null=True)),
                ('family_id', models.CharField(blank=True, max_length=5, null=True)),
                ('is_accepted_name', models.IntegerField(blank=True, null=True)),
                ('provider_id', models.SmallIntegerField(blank=True, null=True)),
                ('ref_short', models.CharField(blank=True, max_length=200, null=True)),
                ('reference', models.TextField(blank=True, null=True)),
                ('is_endemic', models.IntegerField(blank=True, null=True)),
                ('is_alien', models.IntegerField(blank=True, null=True)),
                ('is_fossil', models.IntegerField(blank=True, null=True)),
                ('suggested_link', models.CharField(blank=True, max_length=50, null=True)),
                ('is_photo', models.IntegerField(blank=True, null=True)),
                ('lastmodifiedby', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'scientific_names',
                'managed': False,
            },
        ),
    ]
