# Generated by Django 2.2.13 on 2020-10-05 06:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0028_auto_20201005_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 5, 6, 13, 18, 690550, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 5, 6, 13, 18, 675535, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 5, 6, 13, 18, 677531, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 5, 6, 13, 18, 680540, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 5, 6, 13, 18, 682564, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 5, 6, 13, 18, 687547, tzinfo=utc)),
        ),
    ]