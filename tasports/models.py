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

class Wizards(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Jazz(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Raptors(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Spurs(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Kings(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Trailblazers(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Suns(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Philadelphia(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Magic(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Thunder(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Knicks(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Pelicans(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Timberwolves(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Bucks(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Heat(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Grizzlies(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Lakers(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Clippers(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Pacers(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Rockets(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Warriors(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Pistons(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Nuggets(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Mavericks(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Cavaliers(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Bulls(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Hornets(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Nets(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Celtics(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

class Hawks(models.Model):
    hometeam_src = models.CharField(max_length=100)
    hometeam_id = models.IntegerField()
    hometeam_name = models.CharField(max_length=100)
    fulldatetime = models.CharField(max_length=100)
    awayteam_id = models.IntegerField()
    awayteam_name = models.CharField(max_length=100)
    awayteam_src = models.CharField(max_length=100)

allteams = [Wizards, Jazz, Raptors, Spurs, Kings, Trailblazers, Suns, Philadelphia, Magic, Thunder, Knicks, Pelicans, Timberwolves, Bucks, Heat, Grizzlies, Lakers, Clippers, Pacers, Rockets, Warriors, Pistons, Nuggets, Mavericks, Cavaliers, Bulls, Hornets, Nets, Celtics, Hawks]

# Create your models here.
