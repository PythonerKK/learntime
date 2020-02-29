# Generated by Django 2.2.6 on 2020-02-28 16:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0011_auto_20191203_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='credit_type',
            field=models.CharField(blank=True, choices=[('n', '未选择'), ('fl_credit', '法律'), ('wt_credit', '文体'), ('xl_credit', '心理'), ('cxcy_credit', '创新创业'), ('sxdd_credit', '思想道德')], default='n', max_length=20, null=True, verbose_name='学时类别'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='活动描述'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='join_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '参赛者'), (2, '观众'), (3, '工作人员')], default=2, null=True, verbose_name='参与身份'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='activity/logo/%Y/%m/%d/', verbose_name='活动图标'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='活动名称'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='nums',
            field=models.IntegerField(blank=True, help_text='若无名额限制，请不要填写该内容', null=True, verbose_name='人数上限'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='活动地点'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='score',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='学时'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='sponsor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='主办方'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='活动时间'),
        ),
    ]
