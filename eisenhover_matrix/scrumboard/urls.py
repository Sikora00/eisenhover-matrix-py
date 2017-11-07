from django.conf.urls import url

from .api import TaskApi

urlpatterns = [
    url(r'^task$', TaskApi.as_view())
]
