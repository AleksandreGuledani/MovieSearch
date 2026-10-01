from django.db import models
from django.contrib.auth.models import User

class MovieSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    movie_name = models.CharField(max_length=255)  
    search_time = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.movie_name