# Generated by Django 2.1.7 on 2019-03-23 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190323_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdnkdata',
            name='bdnk_device_data_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.BdnkDeviceIdInfo'),
        ),
    ]