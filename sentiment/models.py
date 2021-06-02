from django.db import models

# Create your models here.
class Review(models.Model):
    ReviewId = models.CharField(max_length=120)
    OverallRating = models.FloatField ()
    Service = models.IntegerField()
    Cleanliness = models.IntegerField()
    Value = models.IntegerField()
    Location = models.IntegerField()
    Result = models.CharField(max_length=120)