from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=100)
    logopath = models.CharField(max_length=100)

    def __str__(self):
        return self.FullName

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    favouriteteams = models.ManyToManyField(Teams)

def __str__(self):
        return self.username

USERNAME_FIELD = 'username'

class Game(models.Model):
    Gameid=models.AutoField(primary_key=True)
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)


# Create your models here.
