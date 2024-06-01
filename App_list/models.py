from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Striming(models.Model):
    Platform = models.CharField(max_length=50)
    Category = models.CharField(max_length=78)
    Site_link = models.URLField()
    active = models.BooleanField(default=True)
    def _str_(self):
        return self.Platform





class WatchList(models.Model):
    MovieName = models.CharField(max_length=50)
    Ratting= models.IntegerField()
    Postal = models.ForeignKey(Striming, on_delete=models.CASCADE, related_name = "WatchList")
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)


    active = models.BooleanField(default=True)
    Story_line = models.CharField(max_length=500)
    Type = models.CharField(max_length=60)
    
    


    def _str_(self):
        return self.MovieName


class Public(models.Model):

   #Public_user = models.ForeignKey(User, on_delete= models.CASCADE)

    review = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    opnion = models.CharField(max_length=3992)
    watchlist = models.ForeignKey(WatchList, on_delete= models.CASCADE, related_name= "Review")
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(
            self.review
        ) + " | " + self.watchlist.MovieName
