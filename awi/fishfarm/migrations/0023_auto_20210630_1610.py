# Generated by Django 3.2.3 on 2021-06-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0022_alter_req_info_grandtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereproduct',
            name='Name_Costomer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='ordereproduct',
            name='CustomerID',
        ),
        migrations.AddField(
            model_name='ordereproduct',
            name='CustomerID',
            field=models.IntegerField(null=True),
        ),
    ]
