# Generated by Django 3.2.3 on 2021-06-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0006_alter_about_us_person_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Fathe_name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('D_O_B', models.DateField()),
                ('sex', models.EmailField(max_length=100)),
                ('type', models.EmailField(max_length=100)),
                ('Feedback', models.CharField(max_length=1000)),
            ],
        ),
    ]
