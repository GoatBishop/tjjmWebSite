# Generated by Django 2.2.13 on 2020-10-04 01:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0014_auto_20201004_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 1, 2, 56, 864742, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 1, 2, 56, 866714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='judge',
            name='judge_name',
            field=models.CharField(default='无', max_length=30, verbose_name='评委姓名'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='judge_type',
            field=models.CharField(default='普通评委', max_length=30, verbose_name='评委类型'),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 1, 2, 56, 868716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 1, 2, 56, 871749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 1, 2, 56, 876753, tzinfo=utc)),
        ),
    ]