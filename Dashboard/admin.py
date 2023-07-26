from django.contrib import admin

from Dashboard.models import Student, Hostel, Room


# Register your models here.
class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'total_rooms')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'room_no', 'space_available')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'matric_no', 'image', 'room')


admin.site.register(Hostel, HostelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Student, StudentAdmin)
