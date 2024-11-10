from rest_framework.permissions import BasePermission

class IsEnrolled(BasePermission):
    def has_object_permissoin(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()