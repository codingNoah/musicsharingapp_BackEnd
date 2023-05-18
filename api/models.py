from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model() 
class Category(models.Model):
    category_title = models.CharField(max_length=20)
    userID = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.category_title


class Music(models.Model):
    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20, choices=[("Pop", "Pop"), ("Rock","Rock"), ("Hip-Hop/Rap","Hip-Hop/Rap"), ("R&B/Soul", "R&B/Soul"), ("Country", "Country"), ("Electronic/Dance", "Electronic/Dance"), ("Jazz", "Jazz"), ("Blues", "Blues"), ("Classical", "Classical" )])
    created_at = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey(user, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.title




class CategoryItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete= models.CASCADE)
