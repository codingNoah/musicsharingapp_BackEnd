from django.contrib import admin
from .models import Music, Category, CategoryItem


class MusicAdmin(admin.ModelAdmin):
    model = Music
    list_display = ["id", "title", "genre", "created_at", "userID"]
    search_fields = ["title"]



class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["id", "category_title", "userID"]
    search_fields = ["title"]


class CategoryItemAdmin(admin.ModelAdmin):
    model = CategoryItem
    list_display = ["id", "music", "category"]
    
    
admin.site.register(Music, MusicAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem, CategoryItemAdmin)