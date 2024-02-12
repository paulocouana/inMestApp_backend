from django.contrib import admin
from .models import IMUser, Cohort, CohortMember

# Register your models here.

admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)
