#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models.signals import pre_delete
from django.db.models.base import ModelBase

from .signals import publisher_pre_delete


class PublishingMeta(ModelBase):
    def __new__(cls, name, bases, attrs):
        model = super(PublishingMeta, cls).__new__(cls, name, bases, attrs)


        if not model._meta.abstract:
            pre_delete.connect(model, publisher_pre_delete)

        return model
