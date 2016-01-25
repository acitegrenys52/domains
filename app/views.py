from rest_framework import permissions
from rest_framework import viewsets

from app.models import Domain
from app.permissions import IsAdminOrReadOnly
from app.serializers import DomainSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
