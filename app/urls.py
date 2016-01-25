from django.conf.urls import url, include
from rest_framework import routers

from app.views import DomainViewSet

router = routers.DefaultRouter()
router.register(r'domains', DomainViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]