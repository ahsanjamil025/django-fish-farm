# Generated by Django 3.2.3 on 2021-06-04 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0007_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='D_O_B',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='Fathe_name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='type',
        ),
    ]
