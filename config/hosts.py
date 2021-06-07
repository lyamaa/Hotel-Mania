from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(r"", settings.ROOT_URLCONF, name="default"),
    host(r"www", settings.ROOT_URLCONF, name="www"),
    host(r"api", "config.urls.hotel", name="hotels"),
    host(r"api", "config.urls.common", name="common"),
    host(r"dj-admin", "config.urls.dj-admin", name="dj-admin"),
)
