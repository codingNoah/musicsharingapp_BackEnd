from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ValidationError
from .models import Music, Category, CategoryItem

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ["username"]


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=40)

    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            raise ValidationError({"username": ["This username already exists."]})
        return super().validate(attrs)


class MusicSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(read_only=True )
    userID = serializers.PrimaryKeyRelatedField(read_only=True )

    class Meta:
        model = Music
        fields = ["id","title","genre", "created_at", "userID"]


class CategorySerializer(serializers.ModelSerializer):

    userID = serializers.PrimaryKeyRelatedField(read_only=True )
    
    class Meta: 
        model = Category 
        fields = ["id", "category_title", "userID"]
    
    


class CategoryItemSerializer(serializers.ModelSerializer):

    # category = serializers.PrimaryKeyRelatedField(read_only=True )
    # music = serializers.PrimaryKeyRelatedField(read_only=True )

    class Meta:
        model = CategoryItem 
        fields = [ "id", "music", "category"]
    

class CategoryMusicSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    music = MusicSerializer()

    class Meta:
        model = CategoryItem
        fields = ["id" , "music", "category"]


class MusicDetailSerializer(serializers.ModelSerializer):
    userID = UserSerializer()

    class Meta:
        model = Music
        fields = ["id","title","genre", "created_at", "userID"]
