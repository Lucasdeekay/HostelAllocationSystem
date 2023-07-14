from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Hostel(models.Model):
    name = models.CharField(max_length=125, choices=[
                ('REHOBOTH', 'REHOBOTH'),
                ('NEW MALE', 'NEW MALE'),
                ('VICTORY', 'VICTORY'),
                ('FAITH', 'FAITH'),
                ('BISHOP', 'BISHOP'),
            ])
    gender = models.CharField(max_length=1, choices=[
                ('M', 'M'),
                ('F', 'F'),
            ])
    total_rooms = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_no = models.PositiveIntegerField()
    space_available = models.PositiveIntegerField(default=6)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    matric_no = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=[
        ('M', 'M'),
        ('F', 'F'),
    ])
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.matric_no
