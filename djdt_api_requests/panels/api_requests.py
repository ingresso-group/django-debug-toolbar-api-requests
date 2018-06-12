# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from debug_toolbar.panels import Panel
from django.utils.translation import ugettext_lazy as _, ungettext

import requests.sessions


def patch_send(send_method, panel):

    def patched_send(self, request, **kwargs):
        response = send_method(self, request, **kwargs)
        panel.record(
            method=request.method,
            url=request.url,
            status_code=response.status_code,
            elapsed=(1000 * response.elapsed.total_seconds())
        )
        return response
    return patched_send


class ApiRequestsPanel(Panel):
    nav_title = 'API Requests'

    title = 'API Requests'

    template = 'djdt_api_requests/panels/api_requests.html'

    def __init__(self, *args, **kwargs):
        super(ApiRequestsPanel, self).__init__(*args, **kwargs)
        self._saved_send = None
        self._requests = []

    def record(self, **kwargs):
        self._requests.append(kwargs)

    @property
    def nav_subtitle(self):
        total_time = sum(r['elapsed'] for r in self._requests)
        num_requests = len(self._requests)
        return ungettext("%d API request in %.2fms",
                         "%d API requests in %.2fms", num_requests,
                         ) % (len(self._requests), total_time)

    def enable_instrumentation(self):
        # monkeypatch the requests library
        if self._saved_send is None:
            self._saved_send = requests.sessions.Session.send
            requests.sessions.Session.send = patch_send(self._saved_send, self)

    def disable_instrumentation(self):
        # unmonkeypatch the requests library
        if self._saved_send is not None:
            requests.sessions.Session.send = self._saved_send
            self._saved_send = None

    def generate_stats(self, request, response):
        self.record_stats({
            'num_requests': len(self._requests),
            'total_time': sum(r['elapsed'] for r in self._requests),
            'requests': self._requests
        })

