# Generated by Django 5.0.1 on 2024-02-13 11:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='classattendance',
            name='attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attended_classes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classattendance',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_class_attendances', to=settings.AUTH_USER_MODEL),
        ),
    ]
