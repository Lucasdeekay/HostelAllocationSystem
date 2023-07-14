from rest_framework import viewsets

from Dashboard.models import Hostel, Room, Student
from Dashboard.serializers import HostelSerializer, RoomSerializer, StudentSerializer


class HostelViewSet(viewsets.ModelViewSet):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all()


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
