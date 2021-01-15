from django.contrib.auth.models import User, Group
from django.db.models import Q, Subquery, OuterRef
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
from .models import ViewApioutput
import datetime, itertools

def name_code(pk, simple, page, limit):
    try:
        context = []
        scinames = ViewApioutput.objects.filter(name_code=pk)
        if simple == 'True':
            for x in scinames:
                context.append({
                    'name_code': x.name_code,
                    'name': x.name,
                    'is_endemic': x.is_endemic,
                    'alien_status': x.alien_status,
                    'comment': x.comment,
                    'datelastmodified': x.datelastmodified,
                    'family': x.family,
                    'family_c': x.family_c,
                    'common_name': x.common_name,
                    'alternative_name_c': x.alternative_name_c,
                    'iucn_code': x.iucn_code,
                    'cites_code': x.cites_code,
                    'coa_redlist_code': x.coa_redlist_code,
                    'redlist_tw_2017': x.redlist2017
                })

        else:
            for x in scinames:
                context.append({
                    'name_code': x.name_code,
                    'name': x.name,
                    'genus': x.genus,
                    'species': x.species,
                    'infraspecies_marker': x.infraspecies_marker,
                    'infraspecies': x.infraspecies,
                    'infraspecies2_marker': x.infraspecies2_marker,
                    'infraspecies2': x.infraspecies2,
                    'author': x.author,
                    'author2': x.author2,
                    'is_accepted_name': x.is_accepted_name,
                    'accepted_name_code': x.accepted_name_code,
                    'status_id': x.status_id,
                    'is_endemic': x.is_endemic,
                    'alien_status': x.alien_status,
                    'is_marine': x.is_marine,
                    'is_fossil': x.is_fossil,
                    'ref_short': x.ref_short,
                    'reference': x.reference,
                    'comment': x.comment,
                    'datelastmodified': x.datelastmodified,
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
                    'common_name': x.common_name,
                    'alternative_name_c': x.alternative_name_c,
                    'iucn_code': x.iucn_code,
                    'cites_code': x.cites_code,
                    'coa_redlist_code': x.coa_redlist_code,
                    'redlist_tw_2017': x.redlist2017,
                    'redlist_wang': x.redlist_wang,
                    'redlist_chen': x.redlist_chen
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
            scinames = ViewApioutput.objects.filter(name__contains=name).filter(
                datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=1)
        except:
            return 'The date range or accepted name does not exist'
    elif date and accept == 'False':
        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            scinames = ViewApioutput.objects.filter(name__contains=name).filter(
                datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=0)
        except:
            return 'The date range does not exist'
    elif date:

        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            scinames = ViewApioutput.objects.filter(name__contains=name).filter(
                datelastmodified__range=(start_time, end_date))
        except:
            return 'The date range does not exist'
    elif accept == 'True':
        try:
            scinames = ViewApioutput.objects.filter(name__contains=name).filter(is_accepted_name__contains=1)
        except:
            return 'The accepted name does not exist'
    elif accept == 'False':
        try:
            scinames = ViewApioutput.objects.filter(name__contains=name).filter(is_accepted_name__contains=0)
        except:
            return 'The species name does not exist'
    else:
        try:
            scinames = ViewApioutput.objects.filter(name__contains=name)
        except:
            return 'The species name does not exist'
        # check whether in redlist
    context = []
    if simple == 'True':
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
                'family': x.family,
                'family_c': x.family_c,
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017
            })

    else:
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'genus': x.genus,
                'species': x.species,
                'infraspecies_marker': x.infraspecies_marker,
                'infraspecies': x.infraspecies,
                'infraspecies2_marker': x.infraspecies2_marker,
                'infraspecies2': x.infraspecies2,
                'author': x.author,
                'author2': x.author2,
                'is_accepted_name': x.is_accepted_name,
                'accepted_name_code': x.accepted_name_code,
                'status_id': x.status_id,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'is_marine': x.is_marine,
                'is_fossil': x.is_fossil,
                'ref_short': x.ref_short,
                'reference': x.reference,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
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
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017,
                'redlist_wang': x.redlist_wang,
                'redlist_chen': x.redlist_chen
            })
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
            scinames = ViewApioutput.objects.filter(Q(common_name__contains=cname)|Q(alternative_name_c__contains=cname)).filter(
                datelastmodified__range=(start_time, end_date)).filter(
                is_accepted_name__contains=1
            )
        except:
            return 'The date range or accepted name does not exist'
    elif date and accept == 'False':
        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            scinames = ViewApioutput.objects.filter(Q(common_name__contains=cname)|Q(alternative_name_c__contains=cname)).filter(
                datelastmodified__range=(start_time, end_date)).filter(
                is_accepted_name__contains=0
            )
        except:
            return 'The date range does not exist'
    elif date:

        try:
            start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = datetime.date.today()
            scinames = ViewApioutput.objects.filter(Q(common_name__contains=cname)|Q(alternative_name_c__contains=cname)).filter(
                datelastmodified__range=(start_time, end_date))
        except:
            return 'The date range does not exist'
    elif accept == 'True':
        try:
            scinames = ViewApioutput.objects.filter(Q(common_name__contains=cname)|Q(alternative_name_c__contains=cname)).filter(is_accepted_name__contains=1)
        except:
            return 'The accepted name does not exist'
    elif accept == 'False':
        try:
            scinames = ViewApioutput.objects.filter(Q(common_name__contains=cname)|Q(alternative_name_c__contains=cname)).filter(
                is_accepted_name__contains=0)
        except:
            return 'The species name does not exist'
    else:
        try:
            scinames = ViewApioutput.objects.filter(Q(common_name__contains=cname)|Q(alternative_name_c__contains=cname))
        except:
            return 'The species name does not exist'
        # check whether in redlist

    context = []
    if simple == 'True':
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
                'family': x.family,
                'family_c': x.family_c,
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017
            })

    else:
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'genus': x.genus,
                'species': x.species,
                'infraspecies_marker': x.infraspecies_marker,
                'infraspecies': x.infraspecies,
                'infraspecies2_marker': x.infraspecies2_marker,
                'infraspecies2': x.infraspecies2,
                'author': x.author,
                'author2': x.author2,
                'is_accepted_name': x.is_accepted_name,
                'accepted_name_code': x.accepted_name_code,
                'status_id': x.status_id,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'is_marine': x.is_marine,
                'is_fossil': x.is_fossil,
                'ref_short': x.ref_short,
                'reference': x.reference,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
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
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017,
                'redlist_wang': x.redlist_wang,
                'redlist_chen': x.redlist_chen
            })

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
                scinames = ViewApioutput.objects.filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=1)
            except:
                return 'The date range does not exist'
        else:
            try:
                scinames = ViewApioutput.objects.filter(is_accepted_name__contains=1)
            except:
                return 'The input condition does not exist'
    elif accept == 'False':
        if date:
            try:
                start_time = datetime.datetime.strptime(date, "%Y-%m-%d")
                end_date = datetime.date.today()
                scinames = ViewApioutput.objects.filter(
                    datelastmodified__range=(start_time, end_date)).filter(is_accepted_name__contains=0)
            except:
                return 'The date range does not exist'
        else:
            try:
                scinames = ViewApioutput.objects.filter(is_accepted_name__contains=0)
            except:
                return 'The input condition does not exist'
    else:
        return 'The input condition does not exist'
        # check whether in redlist

    context = []
    if simple == 'True':
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
                'family': x.family,
                'family_c': x.family_c,
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017
            })

    else:
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'genus': x.genus,
                'species': x.species,
                'infraspecies_marker': x.infraspecies_marker,
                'infraspecies': x.infraspecies,
                'infraspecies2_marker': x.infraspecies2_marker,
                'infraspecies2': x.infraspecies2,
                'author': x.author,
                'author2': x.author2,
                'is_accepted_name': x.is_accepted_name,
                'accepted_name_code': x.accepted_name_code,
                'status_id': x.status_id,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'is_marine': x.is_marine,
                'is_fossil': x.is_fossil,
                'ref_short': x.ref_short,
                'reference': x.reference,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
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
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017,
                'redlist_wang': x.redlist_wang,
                'redlist_chen': x.redlist_chen
            })

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
        scinames = ViewApioutput.objects.filter(datelastmodified__range=(start_time, end_date))
    except:
        return 'The time range does not exist'
        # check whether in redlist
    context = []
    if simple == 'True':
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
                'family': x.family,
                'family_c': x.family_c,
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017
            })

    else:
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'genus': x.genus,
                'species': x.species,
                'infraspecies_marker': x.infraspecies_marker,
                'infraspecies': x.infraspecies,
                'infraspecies2_marker': x.infraspecies2_marker,
                'infraspecies2': x.infraspecies2,
                'author': x.author,
                'author2': x.author2,
                'is_accepted_name': x.is_accepted_name,
                'accepted_name_code': x.accepted_name_code,
                'status_id': x.status_id,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'is_marine': x.is_marine,
                'is_fossil': x.is_fossil,
                'ref_short': x.ref_short,
                'reference': x.reference,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
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
                'common_name': x.common_name,
                'alternative_name_c': x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017,
                'redlist_wang': x.redlist_wang,
                'redlist_chen': x.redlist_chen
            })

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
            scinames = ViewApioutput.objects.all()
        except:
            raise JsonResponse({'message': 'The time range does not exist'}, status=status.HTTP_404_NOT_FOUND)
            # check whether in redlist
        context = []
        for x in scinames:
            context.append({
                'name_code': x.name_code,
                'name': x.name,
                'is_endemic': x.is_endemic,
                'alien_status': x.alien_status,
                'comment': x.comment,
                'datelastmodified': x.datelastmodified,
                'family': x.family,
                'family_c': x.family_c,
                'common_name': x.common_name,
                'alternative_name_c':x.alternative_name_c,
                'iucn_code': x.iucn_code,
                'cites_code': x.cites_code,
                'coa_redlist_code': x.coa_redlist_code,
                'redlist_tw_2017': x.redlist2017
            })

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






    


    
    



