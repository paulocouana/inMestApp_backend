# Generated by Django 5.0.1 on 2024-02-14 15:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_imuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohortmember',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
