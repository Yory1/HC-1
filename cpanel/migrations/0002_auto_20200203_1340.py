# Generated by Django 2.2.7 on 2020-02-03 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancecompanies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insurancecompanies',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='medicalinstitutions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalinstitutions',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='visitation_type',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Consultation', 'Consultation'), ('Operation', 'Operation'), ('ER', 'ER'), ('Other', 'Other')], db_column='Visitation_Type', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='stakeholders',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], db_column='Gender', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='stakeholders',
            name='stakeholder_type',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Clerk', 'Clerk'), ('Editors', 'Editors')], db_column='Stakeholder_Type', max_length=10, null=True),
        ),
    ]