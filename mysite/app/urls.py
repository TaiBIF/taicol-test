"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app import views, views_old
from rest_framework import routers
from app.views_old import NamecodeViewSet, SpeciesViewSet, CommonViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'namecode', views_old.NamecodeViewSet, basename='namecode')
name_code = NamecodeViewSet.as_view({
    'get': 'name_code'
})
router.register(r'speciesname', views_old.SpeciesViewSet, basename='speciesname')
species_name = SpeciesViewSet.as_view({
    'get': 'species_name'
})
router.register(r'common', views_old.CommonViewSet, basename='common')
common_name = CommonViewSet.as_view({
    'get': 'common_name'
})


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #namecode
    path('v1/', views.NewAPI),
    path('', include(router.urls)),
]
