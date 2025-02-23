from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cricketer(models.Model):
    class PlayerType(models.TextChoices):
        RIGHT_HANDED_BATSMAN = "RHB", "Right-Handed Batsman"
        LEFT_HANDED_BATSMAN = "LHB", "Left-Handed Batsman"
        RIGHT_HANDED_BOWLER = "RHBW", "Right-Handed Bowler"
        LEFT_HANDED_BOWLER = "LHBW", "Left-Handed Bowler"
        ALL_ROUNDER = "ALL", "All-Rounder"
        WICKET_KEEPER = "WK", "Wicket Keeper"

    user = name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    jersey_number = models.IntegerField()
    total_runs = models.IntegerField()
    total_centuries = models.IntegerField()
    total_wickets = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    batting_average = models.FloatField(default=0.0)
    strike_rate = models.FloatField(default=0.0)
    highest_score = models.IntegerField(default=0)
    country = models.CharField(max_length=50)
    is_captain = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Player Type Enum Field
    player_type = models.CharField(
        max_length=5,
        choices=PlayerType.choices,
        default=PlayerType.RIGHT_HANDED_BATSMAN
    )


class collect_img(models.Model):
    user = name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='images/', blank=True)
    file = models.FileField(upload_to='files/', blank=True)
    