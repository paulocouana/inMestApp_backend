from .models import *
from django.contrib import admin
from .models import ClassSchedule, ClassAttendance, Query, QueryComment

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created", "date_modified")

admin.site.register(Course, CourseAdmin) # Calls the Course model, and that means it will now be shown in the admin page
admin.site.register(ClassSchedule) # Calls the ClassSchedule model
admin.site.register(ClassAttendance) # Calls the ClassAttendance model
admin.site.register(Query) # Calls the Query model
admin.site.register(QueryComment) # Calls the QueryComment model
