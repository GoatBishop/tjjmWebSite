# Generated by Django 2.2.13 on 2020-10-03 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0010_auto_20201003_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 26, 8, 620771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 26, 8, 622796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 26, 8, 624798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 26, 8, 627800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='tele_member2',
            field=models.CharField(default='', max_length=11, verbose_name='成员2手机号'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tele_member3',
            field=models.CharField(default='', max_length=11, verbose_name='成员3手机号'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 26, 8, 634786, tzinfo=utc)),
        ),
    ]
