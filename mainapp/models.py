from django.db import models
from django.contrib.auth.models import User

# Создайть класс карс 
# c 5 разными полями
# Создайте сериализаторы
# Создайте views
# Создайте urls
# сделайте 5 запросов на постман get, post, put, patch, delete

class Mersedes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    engine_displacement = models.IntegerField()
    sit_places = models.IntegerField()
    release = models.DateField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
