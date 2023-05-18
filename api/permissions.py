from rest_framework.permissions import BasePermission
from .models import CategoryItem, Category
from .serializer import CategorySerializer, UserSerializer, CreateUserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in ['PATCH', 'PUT', 'DELETE', "GET"]:
            
            if obj.userID != request.user:
                return False
        return True
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    

 
    

class GetOnlyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["DELETE" , "POST", "PATCH", "PUT"]:
            return False 
        return super().has_permission(request, view)