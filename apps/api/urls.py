from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.core.views import *

router = DefaultRouter()
router.register('nid', NIDViewSet, 'nid')

urlpatterns = [
    path('', include(router.urls))
]
