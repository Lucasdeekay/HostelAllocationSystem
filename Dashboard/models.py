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
        return f"{self.hostel.name} - {self.room_no}"


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    matric_no = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=[
        ('M', 'M'),
        ('F', 'F'),
    ])
    programme = models.CharField(max_length=100, default='COMPUTER SCIENCE', choices=[
        ('CYBER SECURITY', 'CYBER SECURITY'),
        ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'),
        ('SOFTWARE ENGINEERING', 'SOFTWARE ENGINEERING'),
        ('MICROBIOLOGY', 'MICROBIOLOGY'),
        ('INDUSTRIAL CHEMISTRY', 'INDUSTRIAL CHEMISTRY'),
        ('BIOCHEMISTRY', 'BIOCHEMISTRY'),
        ('BUSINESS ADMINISTRATION', 'BUSINESS ADMINISTRATION'),
        ('ECONOMICS', 'ECONOMICS'),
        ('ACCOUNTING', 'ACCOUNTING'),
        ('MASS COMMUNICATION', 'MASS COMMUNICATION'),
        ('CRIMINOLOGY', 'CRIMINOLOGY'),
    ])
    image = models.ImageField(upload_to='dashboard/student', blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.matric_no

