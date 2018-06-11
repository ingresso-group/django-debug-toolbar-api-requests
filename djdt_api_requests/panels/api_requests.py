# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from debug_toolbar.panels import Panel
import requests.sessions


def patch_send(send_method, panel):

    def patched_send(self, request, **kwargs):
        response = send_method(self, request, **kwargs)
        panel.record(elapsed=response.elapsed.total_seconds())
        return response
    return patched_send


class ApiRequestsPanel(Panel):
    nav_title = 'API Requests'

    # Content would be good to add in a future version
    has_content = False

    title = 'API Requests'

    def __init__(self, *args, **kwargs):
        super(ApiRequestsPanel, self).__init__(*args, **kwargs)
        self._saved_send = None
        self._num_requests = 0
        self._times = []

    def record(self, elapsed):
        # We will probably want to add URLs to this in the future
        self._num_requests += 1
        self._times.append(elapsed)

    @property
    def nav_subtitle(self):
        total_time = sum(self._times)
        return "%d API requests in %.2fms" % (self._num_requests, 1000 * total_time)

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
            'num_requests': self._num_requests,
            'total_time': sum(self._times)
        })

