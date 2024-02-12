from django.db import models
# from django.contrib.auth.models import User  # For Django's default auth system

# Create your models here.

class UserType(models.TextChoices):
    EIT = 'EIT'
    TEACHING_FELLOW = 'TEACHING_FELLOW'
    ADMIN_STAFF = 'ADMIN_STAFF'
    ADMIN = 'ADMIN'

class IMUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=UserType.choices)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)  # Essential for communication
    phone_number = models.CharField(max_length=20, blank=True)  # Optional
    date_of_birth = models.DateField(blank=True, null=True)  # Optional demographic information
    address = models.TextField(blank=True)  # Optional for physical location

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('IMUser', on_delete=models.CASCADE, related_name='cohort_author')  # Reference the IMUser model
    # author = models.ForeignKey('IMUser', on_self=models.PROTECT)  # Reference the IMUser model

    def __str__(self):
        return f"{self.name} ({self.year})"


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey('IMUser', on_delete=models.CASCADE)  # Reference the IMUser model
    # member = models.ForeignKey('IMUser', on_delete=models.PROTECT)  # Reference the IMUser model
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('IMUser', on_delete=models.CASCADE)  # Reference the IMUser model
    # author = models.ForeignKey('IMUser', on_delete=models.PROTECT)  # Reference the IMUser model
    # member = models.ForeignKey(IMUser, on_delete=models.PROTECT, related_name='cohort_memberships')
    # author = models.ForeignKey(IMUser, on_delete=models.PROTECT, related_name='created_cohort_memberships')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_memberships')
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='created_cohort_memberships')

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.cohort.name}"
