from rest_framework import permissions
from backend.settings import DEBUG


class DevProdAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if DEBUG:
            return True
        else:
            return permissions.IsAuthenticated.has_permission(request, view)
