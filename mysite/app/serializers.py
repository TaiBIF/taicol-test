from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ScientificNames, TableSpecieslist, Details


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ScientificNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificNames
        fields = [
            'name_code',
            'name',
            'genus',
            'species',
            'infraspecies_marker',
            'infraspecies',
            'infraspecies2_marker',
            'infraspecies2',
            'author',
            'author2',
            'is_accepted_name',
            'accepted_name_code',
            'status_id',
            'is_endemic',
            'alien_status',
            'is_marine',
            'is_fossil',
            'ref_short',
            'reference',
            'comment',
            'datelastmodified']

class TableSpecieslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableSpecieslist
        fields = (
            'name_code',
            'kingdom',
            'kingdom_c',
            'phylum',
            'phylum_c',
            'class_field',
            'class_c',
            'order',
            'order_c',
            'family',
            'family_c',
            'genus_c',
            'common_name_c')

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = (
            'name_code',
            'iucn_code',
            'cites_code',
            'coa_redlist_code',
            'redlist_tw_2017',
            'redlist_wang',
            'redlist_chen'
        )
