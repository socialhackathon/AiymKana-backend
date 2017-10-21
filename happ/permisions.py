from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions and write permissions are only allowed to the user who created friend.
        return obj.contact == request.user


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
