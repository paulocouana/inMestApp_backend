# Generated by Django 5.0.2 on 2024-02-22 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_course_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='classschedule',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_schedule', to='main.course'),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='facilitator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_facilitator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='meeting_type',
            field=models.CharField(blank=True, choices=[('Class Sessions', 'Class Session'), ('Well Session', 'Wellness Session'), ('Guest Lecture', 'Guest Lecture')], max_length=20, null=True),
        ),
    ]
