from django.urls import path

from apps.core.views import *


urlpatterns = [
    path('', NIDView.as_view(), name='nid'),
]
