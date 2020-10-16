# Generated by Django 2.2.13 on 2020-10-09 01:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0036_auto_20201009_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status_is_pass',
            field=models.CharField(default='未通过', max_length=20, verbose_name='是否通过'),
        ),
        migrations.AddField(
            model_name='team',
            name='status_is_submit',
            field=models.CharField(default='未报送', max_length=20, verbose_name='是否报送'),
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 1, 40, 58, 399123, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 1, 40, 58, 402153, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 1, 40, 58, 414137, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 1, 40, 58, 404156, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 1, 40, 58, 407158, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 1, 40, 58, 412135, tzinfo=utc)),
        ),
    ]