# Generated by Django 2.2.13 on 2020-10-04 16:08

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0019_auto_20201004_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='paper',
        ),
        migrations.AddField(
            model_name='work',
            name='paper_cc',
            field=models.FileField(null=True, upload_to='cc', validators=[django.core.validators.FileExtensionValidator(['pdf'], message='文件必须为pdf格式')], verbose_name='查重报告pdf版'),
        ),
        migrations.AddField(
            model_name='work',
            name='paper_pdf',
            field=models.FileField(null=True, upload_to='pdf', validators=[django.core.validators.FileExtensionValidator(['pdf'], message='文件必须为pdf格式')], verbose_name='作品pdf版'),
        ),
        migrations.AddField(
            model_name='work',
            name='paper_word',
            field=models.FileField(null=True, upload_to='word', validators=[django.core.validators.FileExtensionValidator(['doc', 'docx'], message='文件必须为doc/docx格式')], verbose_name='作品word版'),
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 16, 8, 8, 921043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 16, 8, 8, 923043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 16, 8, 8, 925046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 16, 8, 8, 927048, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 16, 8, 8, 933053, tzinfo=utc)),
        ),
    ]
