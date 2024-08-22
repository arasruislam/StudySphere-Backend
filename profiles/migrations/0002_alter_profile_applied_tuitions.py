# Generated by Django 5.0.7 on 2024-08-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('tuitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='applied_tuitions',
            field=models.ManyToManyField(through='tuitions.TuitionApplication', to='tuitions.tuition'),
        ),
    ]
