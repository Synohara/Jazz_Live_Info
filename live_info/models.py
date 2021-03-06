from django.db import models

# Create your models here.


class Live(models.Model):
    artist = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    reservation_information = models.CharField(max_length=1000)
    link = models.CharField(max_length=100, null=True)
    ticket_available_date = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)
    charge = models.CharField(max_length=100, null=True)
    member = models.CharField(max_length=1000, null=True)
