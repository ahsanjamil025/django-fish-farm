# Generated by Django 3.2.3 on 2021-06-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0021_ordereproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='req_info',
            name='GrandTotal',
            field=models.FloatField(default='0.00', null=True),
        ),
    ]
