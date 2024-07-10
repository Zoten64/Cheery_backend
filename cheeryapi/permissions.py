from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Checks if the authenticated user is the owner of the object
    Does not work for the User model
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
