from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializer import UserSerializer, CreateUserSerializer, MusicSerializer, CategorySerializer, CategoryItemSerializer, CategoryMusicSerializer, MusicDetailSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Music, Category, CategoryItem
from .permissions import IsOwnerOrReadOnly,  GetOnlyPermission
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import MethodNotAllowed


User = get_user_model()


class CreateUserView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):

        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = User.objects.create_user(username=validated_data["username"], password=validated_data["password"])

        return Response(data=UserSerializer(user).data, status=status.HTTP_201_CREATED)


class MusicViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = MusicSerializer
    queryset = Music.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(userID= self.request.user)

    
class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CategorySerializer 
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        return serializer.save(userID= self.request.user)
    
    def get_queryset(self):
        
        if self.request.method == "GET":
            queryset = Category.objects.filter(userID = self.request.user)
            return queryset
        return super().get_queryset()
    
    
class CategoryItemViewSet(ModelViewSet):
    
    serializer_class = CategoryItemSerializer
    queryset = CategoryItem.objects.all()


class UserMusicViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated, GetOnlyPermission]
    permission_classes = [AllowAny]
    serializer_class = MusicSerializer
    queryset = Music.objects.all()

    def get_queryset(self):
        queryset = Music.objects.filter(userID = self.request.user)
        return queryset


class UserCategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, GetOnlyPermission]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        queryset = Category.objects.filter(userID = self.request.user)
        return queryset


class CategoryMusicViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, GetOnlyPermission]
    serializer_class = CategoryMusicSerializer
    queryset = CategoryItem.objects.all()

    def get_queryset(self):
        print(self.request.query_params)
        categoryID = self.request.query_params.get("categoryID")
        if not categoryID:
            return []
        category = CategorySerializer(Category.objects.filter(id = categoryID).first()).data
        if not category:
            return []
        if category.get("userID") != self.request.user.id:
            return []
        queryset = CategoryItem.objects.filter(category = categoryID)
        return queryset


class MusicDetailViewSet(ModelViewSet):
    permission_classes = [ GetOnlyPermission]
    serializer_class = MusicDetailSerializer
    queryset = Music.objects.all()


class UserDetailViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, GetOnlyPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        
        return User.objects.filter(id=user.id)