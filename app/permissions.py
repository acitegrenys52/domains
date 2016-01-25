from rest_framework import permissions

from app.constants import ALLOWED_LOGIN


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.method == "POST":
            return str(request.user) == ALLOWED_LOGIN
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return str(request.user) == ALLOWED_LOGIN
