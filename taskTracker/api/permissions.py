from rest_framework import permissions

class IsAllowedToPostOnlyToTL(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.user_role == "TM":
            if request.method in ['PUT', 'GET']:
                return True
            return False
        elif request.user.user_role == "TL":
            return True