from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import (
    JsonResponse,
    HttpResponseRedirect,
    Http404,
    HttpResponse,
)

from django.template import loader

from rest_framework.decorators import action
from mysite.pagination import CustomPagination
from .models import ScientificNames, TableSpecieslist, Details
from .serializers import (
    UserSerializer,
    GroupSerializer,
    ScientificNamesSerializer,
    TableSpecieslistSerializer,
    DetailsSerializer)
import datetime

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


'''@api_view(['GET', 'POST', 'DELETE'])
def scinames_list(request):
    if request.method == 'GET':
        scinames = ScientificNames.objects.all()

        name = request.GET.get('name', None)  ## Retrieve all ScientificNames/ find by name from MySQL database
        if name is not None:
            scinames = scinames.filter(name__icontains=name)

        scinames_serializer = ScientificNamesSerializer(scinames, many=True)
        return JsonResponse(scinames_serializer.data, safe=False)
        # 'safe=False' for objects serialization


# GET list of tutorials, POST a new tutorial, DELETE all tutorials


@api_view(['GET', 'PUT', 'DELETE'])
def scinames_detail(request, pk):
    # find tutorial by pk (id)
    try:
        scinames = ScientificNames.objects.get(pk=pk)
    except ScientificNames.DoesNotExist:
        return JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE tutorial


@api_view(['GET'])
def scinames_list_published(request):
    scinames = ScientificNames.objects.filter(is_accepted_name=True)

    if request.method == 'GET':
        scinames_serializer = ScientificNamesSerializer(scinames, many=True)
        return JsonResponse(scinames_serializer.data, safe=False)'''
    
class SpeciesViewSet(viewsets.ModelViewSet):
    """
        #### Find the species by scientificname (no need to type completed name):
        ```/speciesname/Aulodrilus pigueti```

       #### Add other filters:
       1. update date : ```/speciesname/Aulodrilus pigueti/date=2011-01-09```
        2. is accepted name: ```/speciesname/Aulodrilus pigueti/accept=True```
        3. combined above criteria (date first, then accept): ```/speciesname/Aulodrilus pigueti/date=2011-01-09/accept=True```
        4. generate the simple format: add ```simple=True``` at last


          """
    queryset = ScientificNames.objects.all()
    serializer_class = ScientificNamesSerializer

    @action(methods=['get'], detail=True, url_path='species-name', url_name='species_name')
    def species_name(self, request, name, accept=None, date=None, simple=None):
        if date and accept == 'True':
            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                scinames = ScientificNames.objects.filter(name__contains=name).filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=1)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif date and accept == 'False':
            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                scinames = ScientificNames.objects.filter(name__contains=name).filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=0)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif date:

            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                scinames = ScientificNames.objects.filter(name__contains=name).filter(
                    datelastmodified__range=(start_time, end_date))
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif accept == 'True':
            try:
                scinames = ScientificNames.objects.filter(name__contains=name).filter(is_accepted_name__contains=1)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif accept == 'False':
            try:
                scinames = ScientificNames.objects.filter(name__contains=name).filter(is_accepted_name__contains=0)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                scinames = ScientificNames.objects.filter(name__contains=name)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # check whether in redlist
        redlist = Details.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        context = []
        if simple == 'True':
            if redlist:
                for x, y, z in zip(tables, scinames, redlist):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'family': x.family,
                        'family_c': x.family_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': z.iucn_code,
                        'cites_code': z.cites_code,
                        'coa_redlist_code': z.coa_redlist_code,
                        'redlist_tw_2017': z.redlist_tw_2017,

                    })
            else:
                for x, y in zip(tables, scinames):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'family': x.family,
                        'family_c': x.family_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': None,
                        'cites_code': None,
                        'coa_redlist_code': None,
                        'redlist_tw_2017': None,

                    })
        else:
            if redlist:
                for x, y, z in zip(tables, scinames, redlist):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'genus': y.genus,
                        'species': y.species,
                        'infraspecies_marker': y.infraspecies_marker,
                        'infraspecies': y.infraspecies,
                        'infraspecies2_marker': y.infraspecies2_marker,
                        'infraspecies2': y.infraspecies2,
                        'author': y.author,
                        'author2': y.author2,
                        'is_accepted_name': y.is_accepted_name,
                        'accepted_name_code': y.accepted_name_code,
                        'status_id': y.status_id,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'is_marine': y.is_marine,
                        'is_fossil': y.is_fossil,
                        'ref_short': y.ref_short,
                        'reference': y.reference,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'kingdom': x.kingdom,
                        'kingdom_c': x.kingdom_c,
                        'phylum': x.phylum,
                        'phylum_c': x.phylum_c,
                        'class': x.class_field,
                        'class_c': x.class_c,
                        'order': x.order,
                        'order_c': x.order_c,
                        'family': x.family,
                        'family_c': x.family_c,
                        'genus_c': x.genus_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': z.iucn_code,
                        'cites_code': z.cites_code,
                        'coa_redlist_code': z.coa_redlist_code,
                        'redlist_tw_2017': z.redlist_tw_2017,
                        'redlist_wang': z.redlist_wang,
                        'redlist_chen': z.redlist_chen
                    })
            else:
                for x, y in zip(
                        TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True)),
                        scinames):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'genus': y.genus,
                        'species': y.species,
                        'infraspecies_marker': y.infraspecies_marker,
                        'infraspecies': y.infraspecies,
                        'infraspecies2_marker': y.infraspecies2_marker,
                        'infraspecies2': y.infraspecies2,
                        'author': y.author,
                        'author2': y.author2,
                        'is_accepted_name': y.is_accepted_name,
                        'accepted_name_code': y.accepted_name_code,
                        'status_id': y.status_id,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'is_marine': y.is_marine,
                        'is_fossil': y.is_fossil,
                        'ref_short': y.ref_short,
                        'reference': y.reference,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'kingdom': x.kingdom,
                        'kingdom_c': x.kingdom_c,
                        'phylum': x.phylum,
                        'phylum_c': x.phylum_c,
                        'class': x.class_field,
                        'class_c': x.class_c,
                        'order': x.order,
                        'order_c': x.order_c,
                        'family': x.family,
                        'family_c': x.family_c,
                        'genus_c': x.genus_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': None,
                        'cites_code': None,
                        'coa_redlist_code': None,
                        'redlist_tw_2017': None,
                        'redlist_wang': None,
                        'redlist_chen': None
                    })

        paginator = Paginator(context, 200, orphans=5)
        num_pages = paginator.num_pages
        # print(num_pages)
        # is_paginated = True if paginator.num_pages > 1 else False
        page = request.GET.get('page')
        if page:
            if int(page) <= num_pages:
                try:
                    current_page = paginator.page(page)
                    current_page_list = current_page.object_list
                except:
                    raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    current_page = paginator.page(1)
                    current_page_list = current_page.object_list
                except:
                    raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                current_page = paginator.page(1)
                current_page_list = current_page.object_list
            except:
                raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response(current_page_list)



class NamecodeViewSet(viewsets.ModelViewSet):
    """
    #### Find the species by namecode:
    ```/namecode/403245```

    #### Generate the simple format : add ```simple=True``` at last
    ```/namecode/403245/simple=True```

       """
    queryset = ScientificNames.objects.all()
    serializer_class = ScientificNamesSerializer

    @action(methods=['get'], detail=True, url_path='name-code', url_name='name_code')
    def name_code(self, request, pk, simple=None):
        try:

            context = []
            scinames = ScientificNames.objects.filter(name_code=pk)
            tables = TableSpecieslist.objects.filter(name_code=pk)
            # check whether in redlist
            redlist = Details.objects.filter(name_code=pk)
            # with redlist
            if simple == 'True':
                if redlist:
                    for x, y, z in zip(tables, scinames, redlist):
                        context.append({
                            'name_code': x.name_code,
                            'name': y.name,
                            'is_endemic': y.is_endemic,
                            'alien_status': y.alien_status,
                            'comment': y.comment,
                            'datelastmodified': y.datelastmodified,
                            'family': x.family,
                            'family_c': x.family_c,
                            'common_name_c': x.common_name_c,
                            'iucn_code': z.iucn_code,
                            'cites_code': z.cites_code,
                            'coa_redlist_code': z.coa_redlist_code,
                            'redlist_tw_2017': z.redlist_tw_2017,

                        })
                else:
                    for x, y in zip(tables, scinames):
                        context.append({
                            'name_code': x.name_code,
                            'name': y.name,
                            'is_endemic': y.is_endemic,
                            'alien_status': y.alien_status,
                            'comment': y.comment,
                            'datelastmodified': y.datelastmodified,
                            'family': x.family,
                            'family_c': x.family_c,
                            'common_name_c': x.common_name_c,
                            'iucn_code': None,
                            'cites_code': None,
                            'coa_redlist_code': None,
                            'redlist_tw_2017': None,

                        })
            else:
                if redlist:
                    for x, y, z in zip(tables, scinames, redlist):
                        context.append({
                            'name_code': x.name_code,
                            'name': y.name,
                            'genus': y.genus,
                            'species': y.species,
                            'infraspecies_marker': y.infraspecies_marker,
                            'infraspecies': y.infraspecies,
                            'infraspecies2_marker': y.infraspecies2_marker,
                            'infraspecies2': y.infraspecies2,
                            'author': y.author,
                            'author2': y.author2,
                            'is_accepted_name': y.is_accepted_name,
                            'accepted_name_code': y.accepted_name_code,
                            'status_id': y.status_id,
                            'is_endemic': y.is_endemic,
                            'alien_status': y.alien_status,
                            'is_marine': y.is_marine,
                            'is_fossil': y.is_fossil,
                            'ref_short': y.ref_short,
                            'reference': y.reference,
                            'comment': y.comment,
                            'datelastmodified': y.datelastmodified,
                            'kingdom': x.kingdom,
                            'kingdom_c': x.kingdom_c,
                            'phylum': x.phylum,
                            'phylum_c': x.phylum_c,
                            'class': x.class_field,
                            'class_c': x.class_c,
                            'order': x.order,
                            'order_c': x.order_c,
                            'family': x.family,
                            'family_c': x.family_c,
                            'genus_c': x.genus_c,
                            'common_name_c': x.common_name_c,
                            'iucn_code': z.iucn_code,
                            'cites_code': z.cites_code,
                            'coa_redlist_code': z.coa_redlist_code,
                            'redlist_tw_2017': z.redlist_tw_2017,
                            'redlist_wang': z.redlist_wang,
                            'redlist_chen': z.redlist_chen
                        })
                else:
                    for x, y in zip(
                            TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True)),
                            scinames):
                        context.append({
                            'name_code': x.name_code,
                            'name': y.name,
                            'genus': y.genus,
                            'species': y.species,
                            'infraspecies_marker': y.infraspecies_marker,
                            'infraspecies': y.infraspecies,
                            'infraspecies2_marker': y.infraspecies2_marker,
                            'infraspecies2': y.infraspecies2,
                            'author': y.author,
                            'author2': y.author2,
                            'is_accepted_name': y.is_accepted_name,
                            'accepted_name_code': y.accepted_name_code,
                            'status_id': y.status_id,
                            'is_endemic': y.is_endemic,
                            'alien_status': y.alien_status,
                            'is_marine': y.is_marine,
                            'is_fossil': y.is_fossil,
                            'ref_short': y.ref_short,
                            'reference': y.reference,
                            'comment': y.comment,
                            'datelastmodified': y.datelastmodified,
                            'kingdom': x.kingdom,
                            'kingdom_c': x.kingdom_c,
                            'phylum': x.phylum,
                            'phylum_c': x.phylum_c,
                            'class': x.class_field,
                            'class_c': x.class_c,
                            'order': x.order,
                            'order_c': x.order_c,
                            'family': x.family,
                            'family_c': x.family_c,
                            'genus_c': x.genus_c,
                            'common_name_c': x.common_name_c,
                            'iucn_code': None,
                            'cites_code': None,
                            'coa_redlist_code': None,
                            'redlist_tw_2017': None,
                            'redlist_wang': None,
                            'redlist_chen': None
                        })

        except:
            raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        paginator = Paginator(context, 200, orphans=5)
        num_pages = paginator.num_pages
        print(num_pages)
        # is_paginated = True if paginator.num_pages > 1 else False
        page = request.GET.get('page')
        if page:
            if int(page) <= num_pages:
                try:
                    current_page = paginator.page(page)
                    current_page_list = current_page.object_list
                except:
                    raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    current_page = paginator.page(1)
                    current_page_list = current_page.object_list
                except:
                    raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                current_page = paginator.page(1)
                current_page_list = current_page.object_list
            except:
                raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response(current_page_list)

class CommonViewSet(viewsets.ModelViewSet):
    """
            #### Find the species by common name (no need to type completed name):
            ```/common/山柑```

           #### Add other filters:
           1. update date : ```/common/山柑/date=2011-01-09```
            2. is accepted name: ```/common/山柑/accept=True```
            3. combined above criteria (date first, then accept): ```/common/山柑/date=2011-01-09/accept=True```
            4. generate the simple format: add ```simple=True``` at last


              """
    queryset = TableSpecieslist.objects.all()
    serializer_class = TableSpecieslistSerializer

    @action(methods=['get'], detail=True, url_path='common-name', url_name='common_name')
    def common_name(self, request, name, accept=None, date=None, simple=None):

        if date and accept == 'True':
            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                tables = TableSpecieslist.objects.filter(common_name_c__contains=name)
                scinames = ScientificNames.objects.filter(
                    name_code__in=tables.values_list('name_code', flat=True)).filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=1)
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif date and accept == 'False':
            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                tables = TableSpecieslist.objects.filter(common_name_c__contains=name)
                scinames = ScientificNames.objects.filter(
                    name_code__in=tables.values_list('name_code', flat=True)).filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=0)
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif date:

            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                tables = TableSpecieslist.objects.filter(common_name_c__contains=name)
                scinames = ScientificNames.objects.filter(
                    name_code__in=tables.values_list('name_code', flat=True)).filter(
                    datelastmodified__range=(start_time, end_date))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif accept == 'True':
            try:
                tables = TableSpecieslist.objects.filter(common_name_c__contains=name)
                scinames = ScientificNames.objects.filter(
                    name_code__in=tables.values_list('name_code', flat=True)).filter(is_accepted_name__contains=1)
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        elif accept == 'False':
            try:
                tables = TableSpecieslist.objects.filter(common_name_c__contains=name)
                scinames = ScientificNames.objects.filter(
                    name_code__in=tables.values_list('name_code', flat=True)).filter(is_accepted_name__contains=0)
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                tables = TableSpecieslist.objects.filter(common_name_c__contains=name)
                scinames = ScientificNames.objects.filter(name_code__in=tables.values_list('name_code', flat=True))
            except:
                raise JsonResponse({'message': 'The species name does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # check whether in redlist
        redlist = Details.objects.filter(name_code__in=tables.values_list('name_code', flat=True))
        context = []
        if simple == 'True':
            if redlist:
                for x, y, z in zip(tables, scinames, redlist):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'family': x.family,
                        'family_c': x.family_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': z.iucn_code,
                        'cites_code': z.cites_code,
                        'coa_redlist_code': z.coa_redlist_code,
                        'redlist_tw_2017': z.redlist_tw_2017,

                    })
            else:
                for x, y in zip(tables, scinames):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'family': x.family,
                        'family_c': x.family_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': None,
                        'cites_code': None,
                        'coa_redlist_code': None,
                        'redlist_tw_2017': None,

                    })
        else:
            if redlist:
                for x, y, z in zip(tables, scinames, redlist):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'genus': y.genus,
                        'species': y.species,
                        'infraspecies_marker': y.infraspecies_marker,
                        'infraspecies': y.infraspecies,
                        'infraspecies2_marker': y.infraspecies2_marker,
                        'infraspecies2': y.infraspecies2,
                        'author': y.author,
                        'author2': y.author2,
                        'is_accepted_name': y.is_accepted_name,
                        'accepted_name_code': y.accepted_name_code,
                        'status_id': y.status_id,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'is_marine': y.is_marine,
                        'is_fossil': y.is_fossil,
                        'ref_short': y.ref_short,
                        'reference': y.reference,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'kingdom': x.kingdom,
                        'kingdom_c': x.kingdom_c,
                        'phylum': x.phylum,
                        'phylum_c': x.phylum_c,
                        'class': x.class_field,
                        'class_c': x.class_c,
                        'order': x.order,
                        'order_c': x.order_c,
                        'family': x.family,
                        'family_c': x.family_c,
                        'genus_c': x.genus_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': z.iucn_code,
                        'cites_code': z.cites_code,
                        'coa_redlist_code': z.coa_redlist_code,
                        'redlist_tw_2017': z.redlist_tw_2017,
                        'redlist_wang': z.redlist_wang,
                        'redlist_chen': z.redlist_chen
                    })
            else:
                for x, y in zip(
                        TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True)),
                        scinames):
                    context.append({
                        'name_code': x.name_code,
                        'name': y.name,
                        'genus': y.genus,
                        'species': y.species,
                        'infraspecies_marker': y.infraspecies_marker,
                        'infraspecies': y.infraspecies,
                        'infraspecies2_marker': y.infraspecies2_marker,
                        'infraspecies2': y.infraspecies2,
                        'author': y.author,
                        'author2': y.author2,
                        'is_accepted_name': y.is_accepted_name,
                        'accepted_name_code': y.accepted_name_code,
                        'status_id': y.status_id,
                        'is_endemic': y.is_endemic,
                        'alien_status': y.alien_status,
                        'is_marine': y.is_marine,
                        'is_fossil': y.is_fossil,
                        'ref_short': y.ref_short,
                        'reference': y.reference,
                        'comment': y.comment,
                        'datelastmodified': y.datelastmodified,
                        'kingdom': x.kingdom,
                        'kingdom_c': x.kingdom_c,
                        'phylum': x.phylum,
                        'phylum_c': x.phylum_c,
                        'class': x.class_field,
                        'class_c': x.class_c,
                        'order': x.order,
                        'order_c': x.order_c,
                        'family': x.family,
                        'family_c': x.family_c,
                        'genus_c': x.genus_c,
                        'common_name_c': x.common_name_c,
                        'iucn_code': None,
                        'cites_code': None,
                        'coa_redlist_code': None,
                        'redlist_tw_2017': None,
                        'redlist_wang': None,
                        'redlist_chen': None
                    })

        paginator = Paginator(context, 200, orphans=5)
        num_pages = paginator.num_pages
        print(num_pages)
        # is_paginated = True if paginator.num_pages > 1 else False
        page = request.GET.get('page')
        if page:
            if int(page) <= num_pages:
                try:
                    current_page = paginator.page(page)
                    current_page_list = current_page.object_list
                except:
                    raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    current_page = paginator.page(1)
                    current_page_list = current_page.object_list
                except:
                    raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                current_page = paginator.page(1)
                current_page_list = current_page.object_list
            except:
                raise JsonResponse({'message': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response(current_page_list)


    
    



