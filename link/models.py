from django.db import models

class BookMyShow(models.Model):
    Mname = models.CharField(max_length=20)
    Mtime = models.TimeField()
    Mdate = models.DateField()
    Mticket = models.FloatField()
    Popcorn = models.BooleanField(default=False)

