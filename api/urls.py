from django.urls import path, re_path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import  CreateUserView, MusicViewSet, CategoryViewSet, CategoryItemViewSet, UserMusicViewSet, UserCategoryViewSet, CategoryMusicViewSet, MusicDetailViewSet, UserDetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("musics", MusicViewSet)
router.register("categories", CategoryViewSet)
router.register("categoryitems", CategoryItemViewSet)
router.register("usermusics", UserMusicViewSet)
router.register("usercategoires", UserCategoryViewSet)
router.register("categorymusics", CategoryMusicViewSet)
router.register("musicdetail", MusicDetailViewSet)
router.register("userdetail", UserDetailViewSet)



urlpatterns=[
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateUserView.as_view()),
    
    path("", include(router.urls))  
]