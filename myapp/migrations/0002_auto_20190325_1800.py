# Generated by Django 2.1.7 on 2019-03-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdnkdeviceidinfo',
            name='imsi',
            field=models.CharField(default='0000', max_length=20),
        ),
    ]