from rest_framework import permissions
from user_profile.serializers import UserProfileSerializer
from django.contrib.auth.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return obj.user_id == request.user
        except Exception:
            return {"message": "You cannot perform this action"}


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            if request.method in permissions.SAFE_METHODS:
                return True
        else:
            if request.method in permissions.SAFE_METHODS:
                return True
            try:
                return (UserProfileSerializer.get_is_staff(
                    request.user.userprofile, obj
                    ))
            except Exception:
                return {"message": "You cannot perform this action"}


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            if request.method in permissions.SAFE_METHODS:
                return True
        else:
            if request.method in permissions.SAFE_METHODS:
                return True
            return (UserProfileSerializer.get_is_superuser(
                    request.user.userprofile, obj
                    ))


class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser is False:
            return False
        elif request.user.is_superuser:
            return True
