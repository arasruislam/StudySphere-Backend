# Generated by Django 5.0.7 on 2024-08-22 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuition',
            name='is_active',
        ),
    ]
