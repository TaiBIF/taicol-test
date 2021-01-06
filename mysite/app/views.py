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
import datetime, itertools

def name_code(pk, simple, page, limit):
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
        return 'The namecode does not exist'
    try:
        paginator = Paginator(context, limit, orphans=5)
        num_pages = paginator.num_pages
    except:
        return 'The imput condition does not exist'
    # is_paginated = True if paginator.num_pages > 1 else False

    if page:
        if int(page) <= num_pages:
            try:
                current_page = paginator.page(page)
                current_page_list = current_page.object_list
                current_page_list.insert(0, {
                    'total_page': num_pages,
                    'current_page': page
                })
            except:
                return 'Page does not exist'
        else:
            return 'Page does not exist'

    else:
        try:
            current_page = paginator.page(1)
            current_page_list = current_page.object_list
            current_page_list.insert(0, {
                'total_page': num_pages,
                'current_page': 1
            })
        except:
            return 'Page does not exist'

    #print('name_code')
    return current_page_list

def species_name(name, simple, date, accept, page, limit):
    #print('species_name')
    if date and accept == 'True':
        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            scinames = ScientificNames.objects.filter(name__contains=name).filter(
                datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=1)
            tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        except:
            return 'The date range or accepted name does not exist'
    elif date and accept == 'False':
        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            scinames = ScientificNames.objects.filter(name__contains=name).filter(
                datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=0)
            tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        except:
            return 'The date range does not exist'
    elif date:

        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            scinames = ScientificNames.objects.filter(name__contains=name).filter(
                datelastmodified__range=(start_time, end_date))
            tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        except:
            return 'The date range does not exist'
    elif accept == 'True':
        try:
            scinames = ScientificNames.objects.filter(name__contains=name).filter(is_accepted_name__contains=1)
            tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        except:
            return 'The accepted name does not exist'
    elif accept == 'False':
        try:
            scinames = ScientificNames.objects.filter(name__contains=name).filter(is_accepted_name__contains=0)
            tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        except:
            return 'The species name does not exist'
    else:
        try:
            scinames = ScientificNames.objects.filter(name__contains=name)
            tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        except:
            return 'The species name does not exist'
        # check whether in redlist
    redlist = Details.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
    context = []
    #Create a redlist dic for adding redlist info
    red_dict = dict()
    for red in redlist:
        red_dict[red.name_code] = red
    context = []
    if simple == 'True':
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
            })
        #check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            #print('red_code', red_code)
            if red_code in list(red_dict.keys()) :
                #print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None

    else:
        for x, y in zip(tables, scinames):
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
            })
        #check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            #print('red_code', red_code)
            if red_code in list(red_dict.keys()) :
                #print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
                item['redlist_wang'] = red_dict[red_code].redlist_wang
                item['redlist_chen'] = red_dict[red_code].redlist_chen
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None
                item['redlist_wang'] = None
                item['redlist_chen'] = None
    try:
        paginator = Paginator(context, limit, orphans=5)
        num_pages = paginator.num_pages
    except:
        return 'The imput condition does not exist'
    # is_paginated = True if paginator.num_pages > 1 else False

    if page:
        if int(page) <= num_pages:
            try:
                current_page = paginator.page(page)
                current_page_list = current_page.object_list
                current_page_list.insert(0,{
                    'total_page':num_pages,
                    'current_page':page
                })
            except:
                return 'Page does not exist'
        else:
            return 'Page does not exist'

    else:
        try:
            current_page = paginator.page(1)
            current_page_list = current_page.object_list
            current_page_list.insert(0, {
                'total_page': num_pages,
                'current_page': 1
            })
        except:
            return 'Page does not exist'
    #print(current_page_list)
    return current_page_list

def common_name(cname, simple, date, accept, page, limit):
    if date and accept == 'True':
        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            tables = TableSpecieslist.objects.filter(common_name_c__contains=cname)
            scinames = ScientificNames.objects.filter(
                name_code__in=tables.values_list('name_code', flat=True)).filter(
                datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=1)
        except:
            return 'The date range or accepted name does not exist'
    elif date and accept == 'False':
        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            tables = TableSpecieslist.objects.filter(common_name_c__contains=cname)
            scinames = ScientificNames.objects.filter(
                name_code__in=tables.values_list('name_code', flat=True)).filter(
                datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=0)
        except:
            return 'The date range does not exist'
    elif date:

        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            tables = TableSpecieslist.objects.filter(common_name_c__contains=cname)
            scinames = ScientificNames.objects.filter(
                name_code__in=tables.values_list('name_code', flat=True)).filter(
                datelastmodified__range=(start_time, end_date))
        except:
            return 'The date range does not exist'
    elif accept == 'True':
        try:
            tables = TableSpecieslist.objects.filter(common_name_c__contains=cname)
            scinames = ScientificNames.objects.filter(
                name_code__in=tables.values_list('name_code', flat=True)).filter(is_accepted_name__contains=1)
        except:
            return 'The accepted name does not exist'
    elif accept == 'False':
        try:
            tables = TableSpecieslist.objects.filter(common_name_c__contains=cname)
            scinames = ScientificNames.objects.filter(
                name_code__in=tables.values_list('name_code', flat=True)).filter(is_accepted_name__contains=0)
        except:
            return 'The species name does not exist'
    else:
        try:
            tables = TableSpecieslist.objects.filter(common_name_c__contains=cname)
            scinames = ScientificNames.objects.filter(name_code__in=tables.values_list('name_code', flat=True))
        except:
            return 'The species name does not exist'
        # check whether in redlist

    redlist = Details.objects.filter(name_code__in=tables.values_list('name_code', flat=True))
    context = []
    # Create a redlist dic for adding redlist info
    red_dict = dict()
    for red in redlist:
        red_dict[red.name_code] = red
    context = []
    if simple == 'True':
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
            })
        # check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            # print('red_code', red_code)
            if red_code in list(red_dict.keys()):
                # print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None

    else:
        for x, y in zip(tables, scinames):
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
            })
        # check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            # print('red_code', red_code)
            if red_code in list(red_dict.keys()):
                # print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
                item['redlist_wang'] = red_dict[red_code].redlist_wang
                item['redlist_chen'] = red_dict[red_code].redlist_chen
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None
                item['redlist_wang'] = None
                item['redlist_chen'] = None

    try:
        paginator = Paginator(context, limit, orphans=5)
        num_pages = paginator.num_pages
    except:
        return 'The imput condition does not exist'
    # is_paginated = True if paginator.num_pages > 1 else False
    if page:
        if int(page) <= num_pages:
            try:
                current_page = paginator.page(page)
                current_page_list = current_page.object_list
                current_page_list.insert(0, {
                    'total_page': num_pages,
                    'current_page': page
                })
            except:
                return 'Page does not exist'
        else:
            return 'Page does not exist'

    else:
        try:
            current_page = paginator.page(1)
            current_page_list = current_page.object_list
            current_page_list.insert(0, {
                'total_page': num_pages,
                'current_page': 1
            })
        except:
            return 'Page does not exist'
    return current_page_list

def accept_name(accept, simple, date, page, limit):
    if accept == 'True':
        if date:
            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                scinames = ScientificNames.objects.filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=1)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                return 'The date range does not exist'
        else:
            try:
                scinames = ScientificNames.objects.filter(is_accepted_name__contains=1)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                return 'The input condition does not exist'
    elif accept == 'False':
        if date:
            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                scinames = ScientificNames.objects.filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=0)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                return 'The date range does not exist'
        else:
            try:
                scinames = ScientificNames.objects.filter(is_accepted_name__contains=0)
                tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
            except:
                return 'The input condition does not exist'
    else:
        return 'The input condition does not exist'
        # check whether in redlist

    redlist = Details.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
    context = []
    # Create a redlist dic for adding redlist info
    red_dict = dict()
    for red in redlist:
        red_dict[red.name_code] = red
    context = []
    if simple == 'True':
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
            })
        # check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            # print('red_code', red_code)
            if red_code in list(red_dict.keys()):
                # print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None

    else:
        for x, y in zip(tables, scinames):
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
            })
        # check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            # print('red_code', red_code)
            if red_code in list(red_dict.keys()):
                # print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
                item['redlist_wang'] = red_dict[red_code].redlist_wang
                item['redlist_chen'] = red_dict[red_code].redlist_chen
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None
                item['redlist_wang'] = None
                item['redlist_chen'] = None

    try:
        paginator = Paginator(context, limit, orphans=5)
        num_pages = paginator.num_pages
    except:
        return 'The imput condition does not exist'
    # is_paginated = True if paginator.num_pages > 1 else False
    if page:
        if int(page) <= num_pages:
            try:
                current_page = paginator.page(page)
                current_page_list = current_page.object_list
                current_page_list.insert(0, {
                    'total_page': num_pages,
                    'current_page': page
                })
            except:
                return 'Page does not exist'
        else:
            return 'Page does not exist'

    else:
        try:
            current_page = paginator.page(1)
            current_page_list = current_page.object_list
            current_page_list.insert(0, {
                'total_page': num_pages,
                'current_page': 1
            })
        except:
            return 'Page does not exist'
    return current_page_list

def date_range(date, simple, page, limit):
    try:
        start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
        end_date = datetime.date.today()
        scinames = ScientificNames.objects.filter(datelastmodified__range=(start_time, end_date))
        tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
    except:
        return 'The time range does not exist'
        # check whether in redlist
    redlist = Details.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
    context = []
    # Create a redlist dic for adding redlist info
    red_dict = dict()
    for red in redlist:
        red_dict[red.name_code] = red
    context = []
    if simple == 'True':
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
            })
        # check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            # print('red_code', red_code)
            if red_code in list(red_dict.keys()):
                # print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None

    else:
        for x, y in zip(tables, scinames):
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
            })
        # check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            # print('red_code', red_code)
            if red_code in list(red_dict.keys()):
                # print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
                item['redlist_wang'] = red_dict[red_code].redlist_wang
                item['redlist_chen'] = red_dict[red_code].redlist_chen
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None
                item['redlist_wang'] = None
                item['redlist_chen'] = None

    try:
        paginator = Paginator(context, limit, orphans=5)
        num_pages = paginator.num_pages
    except:
        return 'The imput condition does not exist'
    # is_paginated = True if paginator.num_pages > 1 else False
    if page:
        if int(page) <= num_pages:
            try:
                current_page = paginator.page(page)
                current_page_list = current_page.object_list
                current_page_list.insert(0, {
                    'total_page': num_pages,
                    'current_page': page
                })
            except:
                return 'Page does not exist'
        else:
            return 'Page does not exist'

    else:
        try:
            current_page = paginator.page(1)
            current_page_list = current_page.object_list
            current_page_list.insert(0, {
                'total_page': num_pages,
                'current_page': 1
            })
        except:
            return 'Page does not exist'
    return current_page_list

def simple_formate(simple, page, limit):
    if simple == 'True':
        try:
            scinames = ScientificNames.objects.all()
            tables = TableSpecieslist.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        except:
            raise JsonResponse({'message': 'The time range does not exist'}, status=status.HTTP_404_NOT_FOUND)
            # check whether in redlist
        redlist = Details.objects.filter(name_code__in=scinames.values_list('name_code', flat=True))
        # Create a redlist dic for adding redlist info
        red_dict = dict()
        for red in redlist:
            red_dict[red.name_code] = red
        context = []
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
            })
        # check whether redlist is or not
        for item in context:
            red_code = item['name_code']
            # print('red_code', red_code)
            if red_code in list(red_dict.keys()):
                # print(red_dict[red_code])
                item['iucn_code'] = red_dict[red_code].iucn_code
                item['cites_code'] = red_dict[red_code].cites_code
                item['coa_redlist_code'] = red_dict[red_code].coa_redlist_code
                item['redlist_tw_2017'] = red_dict[red_code].redlist_tw_2017
            else:
                item['iucn_code'] = None
                item['cites_code'] = None
                item['coa_redlist_code'] = None
                item['redlist_tw_2017'] = None

        try:
            paginator = Paginator(context, limit, orphans=5)
            num_pages = paginator.num_pages
        except:
            return 'The imput condition does not exist'
        # is_paginated = True if paginator.num_pages > 1 else False
        if page:
            if int(page) <= num_pages:
                try:
                    current_page = paginator.page(page)
                    current_page_list = current_page.object_list
                    current_page_list.insert(0, {
                        'total_page': num_pages,
                        'current_page': page
                    })
                except:
                    return 'Page does not exist'
            else:
                return 'Page does not exist'

        else:
            try:
                current_page = paginator.page(1)
                current_page_list = current_page.object_list
                current_page_list.insert(0, {
                    'total_page': num_pages,
                    'current_page': 1
                })
            except:
                return 'Page does not exist'

        #print('simple_formate')
        return current_page_list



def NewAPI(request):
    pk = request.GET.get('namecode', '')
    name = request.GET.get('speciesname', '')
    cname = request.GET.get('common', '')
    date = request.GET.get('date', '')
    accept = request.GET.get('accept', '')
    simple = request.GET.get('simple', '')
    page = request.GET.get('page', '')
    limit = request.GET.get('limit', 200)
    #print(pk,name,cname,date,accept,simple,page,limit)

    if pk:
        result = name_code(pk, simple, page, limit)

    elif name:
        result = species_name(name, simple, date, accept, page, limit)

    elif cname:
        result = common_name(cname, simple, date, accept, page, limit)
    elif accept:
        result = accept_name(accept, simple, date, page, limit)
    elif date:
        result = date_range(date, simple, page, limit)
    elif simple:
        result = simple_formate(simple, page, limit)


    return JsonResponse(result, safe=False)






    


    
    



