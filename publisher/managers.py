#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet

from .middleware import get_draft_status


class PublisherQuerySet(QuerySet):

    def drafts(self):
        from .models import PublisherModelBase
        return self.filter(publisher_is_draft=PublisherModelBase.STATE_DRAFT)

    def published(self):
        from .models import PublisherModelBase
        return self.filter(publisher_is_draft=PublisherModelBase.STATE_PUBLISHED)

    def current(self):
        if get_draft_status():
            return self.drafts()
        return self.published()
