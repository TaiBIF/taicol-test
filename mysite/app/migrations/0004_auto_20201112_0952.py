# Generated by Django 3.1.3 on 2020-11-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_chorda'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableSpecieslist',
            fields=[
                ('kingdom_id', models.IntegerField(blank=True, null=True)),
                ('kingdom', models.CharField(blank=True, max_length=50, null=True)),
                ('kingdom_c', models.CharField(blank=True, max_length=50, null=True)),
                ('phylum_id', models.CharField(blank=True, max_length=50, null=True)),
                ('phylum', models.CharField(blank=True, max_length=50, null=True)),
                ('phylum_c', models.CharField(blank=True, max_length=50, null=True)),
                ('class_id', models.CharField(blank=True, max_length=50, null=True)),
                ('class_field', models.CharField(blank=True, db_column='class', max_length=50, null=True)),
                ('class_c', models.CharField(blank=True, max_length=50, null=True)),
                ('order_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order', models.CharField(blank=True, max_length=50, null=True)),
                ('order_c', models.CharField(blank=True, max_length=50, null=True)),
                ('family', models.CharField(blank=True, max_length=50, null=True)),
                ('family_c', models.CharField(blank=True, max_length=50, null=True)),
                ('name_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('genus', models.CharField(blank=True, max_length=80, null=True)),
                ('species', models.CharField(blank=True, max_length=100, null=True)),
                ('infraspecies_marker', models.CharField(blank=True, max_length=20, null=True)),
                ('infraspecies', models.CharField(blank=True, max_length=50, null=True)),
                ('infraspecies2_marker', models.CharField(blank=True, max_length=20, null=True)),
                ('infraspecies2', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
                ('author2', models.CharField(blank=True, max_length=150, null=True)),
                ('accepted_name_code', models.CharField(blank=True, max_length=20, null=True)),
                ('status_id', models.IntegerField(blank=True, null=True)),
                ('family_id', models.CharField(blank=True, max_length=5, null=True)),
                ('is_accepted_name', models.IntegerField(blank=True, null=True)),
                ('provider_id', models.SmallIntegerField(blank=True, null=True)),
                ('is_endemic', models.IntegerField(blank=True, null=True)),
                ('is_marine', models.IntegerField(blank=True, null=True)),
                ('alien_status', models.IntegerField(blank=True, null=True)),
                ('is_fossil', models.IntegerField(blank=True, null=True)),
                ('suggested_link', models.CharField(blank=True, max_length=50, null=True)),
                ('common_name_c', models.TextField(blank=True, null=True)),
                ('genus_c', models.CharField(blank=True, max_length=50, null=True)),
                ('is_photo', models.IntegerField(blank=True, null=True)),
                ('datelastmodified', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'table_specieslist',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Chordata',
        ),
        migrations.DeleteModel(
            name='CommonNames',
        ),
        migrations.DeleteModel(
            name='DboTaibnetSpecieslist',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Ob3',
        ),
        migrations.DeleteModel(
            name='Obs',
        ),
        migrations.DeleteModel(
            name='Observation',
        ),
        migrations.DeleteModel(
            name='Observation0623',
        ),
        migrations.DeleteModel(
            name='Observation1',
        ),
        migrations.DeleteModel(
            name='Observation1215',
        ),
        migrations.DeleteModel(
            name='Observation2',
        ),
        migrations.DeleteModel(
            name='Observation20111206',
        ),
        migrations.DeleteModel(
            name='Observation20120717Back',
        ),
        migrations.DeleteModel(
            name='Observation20120816',
        ),
        migrations.DeleteModel(
            name='ObservationTmp',
        ),
        migrations.DeleteModel(
            name='ObsGraph',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.DeleteModel(
            name='Plan0623',
        ),
        migrations.DeleteModel(
            name='Plan2',
        ),
        migrations.DeleteModel(
            name='Plan20111206',
        ),
        migrations.DeleteModel(
            name='Plan20120717Back',
        ),
        migrations.DeleteModel(
            name='Plan20121119',
        ),
        migrations.DeleteModel(
            name='PlanTmp',
        ),
        migrations.DeleteModel(
            name='RegionConfig',
        ),
        migrations.DeleteModel(
            name='RegionCoordinates',
        ),
        migrations.DeleteModel(
            name='RegionNames',
        ),
        migrations.DeleteModel(
            name='Sp2000ScientificNames',
        ),
        migrations.DeleteModel(
            name='SpeciesLists',
        ),
        migrations.DeleteModel(
            name='StationGraph',
        ),
        migrations.DeleteModel(
            name='StationGraph1207',
        ),
        migrations.DeleteModel(
            name='TableClass',
        ),
        migrations.DeleteModel(
            name='TableFamily',
        ),
        migrations.DeleteModel(
            name='TableKingdom',
        ),
        migrations.DeleteModel(
            name='TableName',
        ),
        migrations.DeleteModel(
            name='TableOrder',
        ),
        migrations.DeleteModel(
            name='TablePhylum',
        ),
        migrations.DeleteModel(
            name='TogbifAll',
        ),
        migrations.DeleteModel(
            name='Toipt',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
        migrations.DeleteModel(
            name='Workstation',
        ),
        migrations.DeleteModel(
            name='Workstation0623',
        ),
        migrations.DeleteModel(
            name='Workstation1',
        ),
        migrations.DeleteModel(
            name='Workstation1207',
        ),
        migrations.DeleteModel(
            name='Workstation2',
        ),
        migrations.DeleteModel(
            name='Workstation20111206',
        ),
        migrations.DeleteModel(
            name='Workstation20120717Back',
        ),
        migrations.DeleteModel(
            name='Workstation20120816',
        ),
        migrations.DeleteModel(
            name='Workstation20121129',
        ),
        migrations.DeleteModel(
            name='WorkstationRegionLink',
        ),
        migrations.DeleteModel(
            name='WorkstationTmp',
        ),
    ]
