from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Alow users to edit their own profiles'''

    def has_object_permission(self, request, view, obj):
        '''check user that try to edit their own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
        #return super().has_object_permission(request, view, obj)

class UpdateOwnStatus(permissions.BasePermission):
    '''allow user to update their own feed'''
    def has_object_permission(self, request, view, obj):
        '''check user is trying to update their own status'''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
    