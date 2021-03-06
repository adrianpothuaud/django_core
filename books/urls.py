"""django_core_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views as books_views

app_name = 'books'

urlpatterns = [
    url(r'^search_by_title/$', books_views.search_by_title, name='search_by_title'),
    url(r'^search_by_valid_title/$', books_views.search_by_valid_title, name='search_by_valid_title'),
    url(r'^custom_filters/$', books_views.custom_filters, name='custom_filters'),
    url(r'^custom_tags/$', books_views.custom_tags, name='custom_tags'),
    url(r'^advanced_custom_tags/$', books_views.advanced_custom_tags, name='advanced_custom_tags'),
    url(r'^c2_related_objects/$', books_views.c2_related_objects, name='c2_related_objects'),
    url(r'^c2_model_manager/$', books_views.c2_model_manager, name='c2_model_manager'),
]
