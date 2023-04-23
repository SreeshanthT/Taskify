from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from django.utils.text import slugify 
from django.db import models
from django.apps import apps as django_apps
from django.contrib.contenttypes.models import ContentType 
from django.shortcuts import get_object_or_404

from django_lifecycle import (
    LifecycleModelMixin, hook, AFTER_CREATE, AFTER_SAVE, BEFORE_SAVE, BEFORE_CREATE
)


import re
import random
import string
import json

class ManageBaseView(object):
    method_name = None
    template_name = None
    items_per_page = 10

    def get_template_name(self):
        return self.template_name

    def get(self, request, *args, **kwargs):

        if self.method_name is not None:
            func = getattr(self, self.method_name, None)
            if func is not None:
                return func(request, *args, **kwargs)
        raise Http404("Method Not Allowed")

    def post(self, request, *args, **kwargs):

        if self.method_name is not None:
            func = getattr(self, self.method_name, None)
            if func is not None:
                return func(request, *args, **kwargs)

        raise Http404("Method Not Allowed")

    def get_paginated_items(self, items):
        paginator = Paginator(items, int(self.request.GET.get('records', str(self.items_per_page))))
        page = self.request.GET.get('page', 1)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return items
    
class CustomQuerySet(models.QuerySet):
    def only_active(self, **kwargs):
        return self.filter(active=True, **kwargs)
    
class BaseContent(LifecycleModelMixin, models.Model):
    display_name = 'name'
    slug_field = 'name'

    active = models.BooleanField('Status', default=True, choices=(
        (False, 'Inactive'),
        (True, 'Active')
    ))
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    display_order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(blank=True,max_length=255,db_index=True)
    objects = CustomQuerySet.as_manager()

    class Meta:
        abstract = True

    def __str__(self):
        return str(getattr(self, self.display_name, '') or self.id)

    def get_model_name(self):
        return self.content_type().model

    def content_type(self):
        return ContentType.objects.get_for_model(self)

    def get_values(self, *args, **kwargs):
        try:
            return self.content_type().model_class().objects.filter(id=self.id).values(*args)[0]
        except Exception as e:
            print(e)
            return {}

    def as_dict(self):
        return json.loads(
            serializers.serialize("json", self.__class__.objects.filter(pk=self.id))
        )[0]['fields']

    def as_json(self):
        return self.get_values(fields=self.__class__._meta.get_fields(), json=True)

    def class_name(self):
        return self.__class__.__name__

    def permission_roles(self):
        try:
            PermissionRoles = django_apps.get_model('django_roles_permissions', 'PermissionRoles')
            return PermissionRoles.objects.get(content_type=self.content_type(), object_id=self.id)
        except:
            return None
    
    def get_status(self):
        if self.active:
            return "Active"
        return "Inactive"

    @hook(AFTER_CREATE)
    def slug_generator(self):
        slug_data = getattr(self, self.slug_field, '') or string_manipulation(self.__str__()) or self.id
        self.slug = unique_slug_generator(self, slug_data)
        self.save()


def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))
   
def unique_slug_generator(instance,slugField, new_slug = None, size=4): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(slugField) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = size)) 
              
        return unique_slug_generator(instance,slugField, new_slug = new_slug) 
    return slug 

def get_object_or_none(query, **kwargs):
    try:
        return get_object_or_404(query, **kwargs)
    except:
        return None


def string_manipulation(my_string, replace="!?: ,"):
    replacer = r"[" + replace + "]"
    return re.sub(replacer, "_", my_string).rstrip("_").lower()
