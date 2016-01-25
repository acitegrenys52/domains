from rest_framework import permissions

from app.constants import ALLOWED_LOGIN


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ('POST', 'PATCH', 'PUT'):
            return str(request.user) == ALLOWED_LOGIN
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return str(request.user) == ALLOWED_LOGIN
