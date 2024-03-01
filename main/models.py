from django.db import models
from users.models import Cohort, IMUser

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 1000, blank = True, null = True) # creates the table that we want to register
    description = models.TextField(default = '', blank = True, null = True) # It just 
    date_created = models.DateTimeField(auto_now_add = True, blank = True, null = True) # Anytime anything is inserted, update the date
    date_modified = models.DateTimeField(auto_now = True, blank = True, null = True) # The moment something is added include the current date


class RepeatFrequency(models.TextChoices):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    BIWEEKLY = 'BIWEEKLY'
    MONTHLY = 'MONTHLY'


class MeetingTypes(models.TextChoices):
    CLASS_SESSION = 'Class Sessions'
    WELLNESS_SESSION = 'Well Session'
    GUEST_LECTURE = 'Guest Lecture'

class ClassSchedule(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=10, choices=RepeatFrequency.choices, blank=True, null=True)
    meeting_type = models.CharField(max_length=20, choices=MeetingTypes.choices, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='organized_schedule')  # Reference the IMUser model
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, blank=True, null=True)  # Optional reference to Cohort
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null= True, related_name='course_schedule')
    facilitator = models.ForeignKey(IMUser, on_delete=models.CASCADE, blank=True, null= True, related_name='class_facilitator')
    venue = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return f"{self.title} ({self.start_date_and_time} - {self.end_date_and_time})"


class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE)  # Reference the IMUser model
    is_present = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    attendee = models.ForeignKey(IMUser, on_delete=models.PROTECT, related_name='attended_classes')
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='created_class_attendances')  # Reference the IMUser model
    
    def __str__(self):
        return f"{self.attendee.first_name} {self.attendee.last_name} - {self.class_schedule.title}"

    # The related_name helps me prefetch data and get the results I am looking for very quickly. I can just use author_id to fetch all the data related to an specific id and return the selected data quickly

class ResolutionStatus(models.TextChoices):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    DECLINED = 'DECLINED'
    RESOLVED = 'RESOLVED'


class Query(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries')  # Reference the IMUser model
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='assigned_queries', blank=True, null=True)  # Optional assignment
    resolution_status = models.CharField(max_length=20, choices=ResolutionStatus.choices, default=ResolutionStatus.PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='author_queries')  # Reference the IMUser model

    def __str__(self):
        return f"{self.title} ({self.resolution_status})"


class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='author_query_comments')  # Reference the IMUser model

    def __str__(self):
        return f"{self.query.title} - {self.comment[:20]}"
