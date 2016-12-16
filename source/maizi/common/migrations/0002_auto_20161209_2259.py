# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image_url',
            field=models.ImageField(verbose_name='图片路径', upload_to='ad/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='careercourse',
            name='image',
            field=models.ImageField(verbose_name='课程小图标', upload_to='course/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(verbose_name='课程封面', upload_to='course/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='download_url',
            field=models.FileField(verbose_name='下载地址', upload_to='course/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lessonresource',
            name='download_url',
            field=models.FileField(verbose_name='下载地址', upload_to='lesson/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='links',
            name='image_url',
            field=models.ImageField(null=True, verbose_name='图片路径', upload_to='links/%Y/%m', blank=True),
        ),
        migrations.AlterField(
            model_name='mymessage',
            name='action_type',
            field=models.CharField(verbose_name='类型', choices=[('1', '系统消息'), ('2', '课程讨论回复'), ('3', '论坛讨论回复')], max_length=1),
        ),
        migrations.AlterField(
            model_name='recommendedreading',
            name='reading_type',
            field=models.CharField(verbose_name='文章类型', choices=[('AV', '官方活动'), ('NW', '开发者资讯'), ('DC', '技术交流')], default='AV', max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_middle_thumbnall',
            field=models.ImageField(verbose_name='头像104x104', max_length=200, default='avatar/default_middle.png', null=True, upload_to='avatar/%Y/%m', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_small_thumbnall',
            field=models.ImageField(verbose_name='头像70x70', max_length=200, default='avatar/default_small.png', null=True, upload_to='avatar/%Y/%m', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_url',
            field=models.ImageField(verbose_name='头像220x220', max_length=200, default='avatar/default_big.png', null=True, upload_to='avatar/%Y/%m', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(verbose_name='是否激活', help_text='用户是否被激活，未激活则不能使用', default=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(verbose_name='职员状态', help_text='是否能够登录管理后台', default=False),
        ),
    ]
