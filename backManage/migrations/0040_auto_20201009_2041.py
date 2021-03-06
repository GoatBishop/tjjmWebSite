# Generated by Django 2.2.13 on 2020-10-09 12:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0039_auto_20201009_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status_is_review',
            field=models.CharField(default='否', max_length=20, verbose_name='是否提交评分'),
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 12, 41, 40, 627240, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 12, 41, 40, 629231, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 12, 41, 40, 642243, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 12, 41, 40, 631233, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 12, 41, 40, 634236, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 12, 41, 40, 640242, tzinfo=utc)),
        ),
    ]
