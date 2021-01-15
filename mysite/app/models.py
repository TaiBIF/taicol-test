# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ScientificNames(models.Model):
    name_code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    is_marine = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'scientific_names'

class TableSpecieslist(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=50)
    common_name_c = models.TextField(blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'table_specieslist'

class Details(models.Model):
    name_code = models.CharField(primary_key=True, max_length=255)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    redlist_tw_2017 = models.CharField(db_column='redlist2017', max_length=10, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details'

class ViewAlternativeNameC(models.Model):
    name_code = models.CharField(primary_key=True, max_length=255)
    alternative_name_c = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_alternative_name_c'


class ViewApioutput(models.Model):
    name_code = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_marine = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    common_name = models.CharField(max_length=255, blank=True, null=True)
    alternative_name_c = models.TextField(blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    redlist2017 = models.CharField(max_length=10, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_apioutput'