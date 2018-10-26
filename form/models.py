from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class Room(models.Model):
    room_number = models.IntegerField()

    def __str__(self):
        return (str)(self.room_number)

    def get_absolute_url(self):
        return reverse('room_detail', kwargs={'pk': self.pk})


class Customer(models.Model):
    name= models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField(blank=True)
    dateofjoining = models.DateTimeField(default=datetime.now, blank=True)
    duration = models.IntegerField()
    fee = models.IntegerField()
    checkout= models.BooleanField(blank=True)
    room_number= models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

