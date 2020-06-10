from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    Movie_name = models.CharField(max_length=40)
    Date = models.DateField(blank=False)


class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Tickets = models.DecimalField(max_digits=4, decimal_places=2)
    time = models.TimeField()

    def __str__(self):
        return str(self.time)+self.movie.Movie_name

# class Show(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     time = models.TimeField()
