# Generated by Django 2.2.7 on 2020-02-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0002_auto_20200203_1340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicalInstitutionsAdress',
            new_name='MedicalInstitutionsAddress',
        ),
        migrations.AddField(
            model_name='patient',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]