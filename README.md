Django Debug Toolbar API Requests Panel
=======================================

What does it do
---------------
This adds a panel to the
[Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
that hooks into the [Requests](https://github.com/requests/requests) library
and records useful information about API requests that are made by your
application.


How to Use
----------
Install using `pip`
<!-- TODO: put into PyPI  -->

```shell
pip install git+https://github.com/ingresso-group/django-debug-toolbar-api-requests.git
```

Then add to the debug toolbar panels setting to your django apps `settings.py`

```python
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'djdt_api_requests.panels.ApiRequestsPanel', # Fits quite nicely here
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
```
