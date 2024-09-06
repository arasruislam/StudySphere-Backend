# Generated by Django 5.0.7 on 2024-09-05 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructor', '0002_alter_instructor_gender'),
        ('student', '0002_student_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('availability', models.BooleanField(default=True)),
                ('tuition_class', models.CharField(choices=[('Class 1', 'Class 1'), ('Class 2', 'Class 2'), ('Class 3', 'Class 3'), ('Class 4', 'Class 4'), ('Class 5', 'Class 5'), ('Class 6', 'Class 6'), ('Class 7', 'Class 7'), ('Class 8', 'Class 8'), ('Class 9', 'Class 9'), ('Class 10', 'Class 10'), ('HSC 1', 'HSC 1st Year'), ('HSC 2', 'HSC 2nd Year')], max_length=50)),
                ('medium', models.CharField(choices=[('Both', 'Both'), ('Bangla', 'Bangla Medium'), ('English', 'English Medium')], max_length=50)),
                ('student_gender', models.CharField(choices=[('Both', 'Both'), ('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('preferred_tutor_gender', models.CharField(choices=[('Both', 'Both'), ('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('tutoring_time', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=20)),
                ('number_of_students', models.PositiveIntegerField(default=1)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuitions', to='instructor.instructor')),
                ('subject', models.ManyToManyField(related_name='tuitions', to='tuitions.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='student.student')),
                ('tuition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tuitions.tuition')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('tuition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuitions.tuition')),
            ],
        ),
    ]
