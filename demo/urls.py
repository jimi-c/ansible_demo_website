from django.conf.urls import include, url

from health.views import health

urlpatterns = [
    url(r'^health$', health),
    url(r'', include('main.urls', namespace='main')),
]
