# Generated by Django 2.1.2 on 2018-10-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20181022_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]