# Generated by Django 2.2.7 on 2020-02-25 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vezeeta', '0003_auto_20200225_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicpatientbooking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='clinicpatientbooking',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='hospitalpatientbooking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='hospitalpatientbooking',
            name='updated_at',
        ),
    ]