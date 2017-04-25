#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local


try:
    from django.utils.deprecation import MiddlewareMixin
    parent = MiddlewareMixin
except ImportError:
    parent = object


_thread_locals = local()


def get_draft_status():
    return getattr(_thread_locals, 'is_draft', False)


class PublisherMiddleware(parent):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def is_draft(self, request):
        authenticated = request.user.is_authenticated() and request.user.is_staff
        is_draft = 'edit' in request.GET and authenticated
        return is_draft

    def process_request(self, request):
        _thread_locals.is_draft = self.is_draft(request)

    def process_response(self, request, response):
        if hasattr(_thread_locals, 'is_draft'):
            del _thread_locals.is_draft
        return response
