# Generated by Django 5.0.7 on 2024-09-04 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.URLField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('tuition_area', models.CharField(max_length=200)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Not_Available', 'Not Available')], default='Available', max_length=20)),
                ('days_per_week', models.IntegerField(default=5)),
                ('experience', models.CharField(max_length=20)),
                ('extra_facilities', models.CharField(max_length=200)),
                ('medium_of_instruction', models.CharField(choices=[('Both', 'Both'), ('Bangla', 'Bangla Medium'), ('English', 'English Medium')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
