# Generated by Django 2.2.7 on 2020-02-24 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0005_auto_20200224_1544'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clinicrating',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='hospitalrating',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='labrating',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='physicianrating',
            unique_together=set(),
        ),
    ]
