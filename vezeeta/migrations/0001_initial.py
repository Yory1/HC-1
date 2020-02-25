# Generated by Django 2.2.7 on 2020-02-25 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpanel', '0006_auto_20200224_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicianPatientBooking',
            fields=[
                ('ID', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('booking_date_clinic', models.DateTimeField(db_column='Booking_Date_clinic')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking_date_hospital', models.DateTimeField(db_column='Booking_Date_Hospital')),
                ('phone', models.CharField(db_column='Phone', max_length=25)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=320, null=True)),
                ('message', models.TextField(blank=True, db_column='Message', null=True)),
                ('clinic', models.ForeignKey(db_column='Clinic_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Clinic')),
                ('hospital', models.ForeignKey(db_column='Hospital_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Hospital')),
                ('patient_nn', models.ForeignKey(db_column='Patient_NN', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Patient')),
                ('physician_nn', models.ForeignKey(db_column='Physician_NN', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Physician')),
            ],
            options={
                'verbose_name': 'Physician Booking',
                'verbose_name_plural': 'Physician Bookings',
                'db_table': 'physician_patient_booking',
            },
        ),
        migrations.CreateModel(
            name='HospitalPatientBooking',
            fields=[
                ('ID', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking_date_hospital', models.DateTimeField(db_column='Booking_Date_Hospital')),
                ('phone', models.CharField(db_column='Phone', max_length=25)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=320, null=True)),
                ('message', models.TextField(blank=True, db_column='Message', null=True)),
                ('hospital', models.ForeignKey(db_column='Hospital_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Hospital')),
                ('patient_nn', models.ForeignKey(db_column='Patient_NN', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Patient')),
                ('physician_nn', models.ForeignKey(db_column='Physician_NN', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Physician')),
            ],
            options={
                'verbose_name': 'Hospital Booking',
                'verbose_name_plural': 'Hospital Bookings',
                'db_table': 'Hospital_patient_booking',
            },
        ),
        migrations.CreateModel(
            name='ClinicPatientBooking',
            fields=[
                ('ID', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('booking_date_clinic', models.DateTimeField(db_column='Booking_Date_clinic')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(db_column='Phone', max_length=25)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=320, null=True)),
                ('message', models.TextField(blank=True, db_column='Message', null=True)),
                ('clinic', models.ForeignKey(db_column='Clinic_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Clinic')),
                ('patient_nn', models.ForeignKey(db_column='Patient_NN', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Patient')),
                ('physician_nn', models.ForeignKey(db_column='Physician_NN', on_delete=django.db.models.deletion.DO_NOTHING, to='cpanel.Physician')),
            ],
            options={
                'verbose_name': 'Clinic Booking',
                'verbose_name_plural': 'Clinic Bookings',
                'db_table': 'clinic_patient_booking',
            },
        ),
    ]
