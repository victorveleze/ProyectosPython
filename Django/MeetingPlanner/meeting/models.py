from django.db import models
from datetime import time

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    roomNumber = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.roomNumber} on floor {self.floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    startTime = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.startTime} on {self.date}"