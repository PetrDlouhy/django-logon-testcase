# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_logon_testcase.urls import urlpatterns as django_logon_testcase_urls

urlpatterns = [
    url(r'^', include(django_logon_testcase_urls, namespace='django_logon_testcase')),
]
