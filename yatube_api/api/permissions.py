from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        method_in_permissions = request.method in permissions.SAFE_METHODS
        return method_in_permissions or obj.author == request.user
