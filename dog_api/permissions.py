from rest_framework import permissions
from user_profile.serializers import UserProfileSerializer
from django.contrib.auth.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return obj.user_id == request.user
        except:
            return {"message": "You cannot perform this action"}
    
# class IsStaffAndOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_anonymous:
#             if request.method in permissions.SAFE_METHODS:
#                 return True
#         elif request.user.is_authenticated:
#             if request.method in permissions.SAFE_METHODS:
#                 return True
#             return (UserProfileSerializer.get_is_staff(request.user.userprofile, obj)) == True
#         else:
#             print("Error in is staff and owner or read only permission")
            
class IsStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            if request.method in permissions.SAFE_METHODS:
                return True
        else:
            if request.method in permissions.SAFE_METHODS:
                return True
            try:
                print(UserProfileSerializer.get_is_staff(request.user.userprofile, obj))
                print("hello")
                return (UserProfileSerializer.get_is_staff(request.user.userprofile, obj))
            except:
                return {"message": "You cannot perform this action"}
    
        
class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            if request.method in permissions.SAFE_METHODS:
                return True
        else:
            if request.method in permissions.SAFE_METHODS:
                return True
            return (UserProfileSerializer.get_is_superuser(request.user.userprofile, obj))
        
        
class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('called')
        if request.user.is_superuser == False:
            print('false')
            return False
        elif request.user.is_superuser:
            print('true')
            return True
        # print(UserProfileSerializer.get_is_superuser(request.user.userprofile, obj))
        # return (UserProfileSerializer.get_is_superuser(request.user.userprofile, obj))
        