# Generated by Django 5.0.7 on 2024-09-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0002_alter_tuition_tuition_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuition',
            name='tuition_class',
            field=models.CharField(choices=[('Class 1', 'Class_1'), ('Class 2', 'Class_2'), ('Class 3', 'Class_3'), ('Class 4', 'Class_4'), ('Class 5', 'Class_5'), ('Class 6', 'Class_6'), ('Class 7', 'Class_7'), ('Class 8', 'Class_8'), ('Class 9', 'Class_9'), ('Class 10', 'Class_10'), ('HSC 1', 'HSC_1st_Year'), ('HSC 2', 'HSC_2nd_Year')], max_length=50),
        ),
    ]
