# Generated by Django 2.2.6 on 2019-11-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleStudent',
            fields=[
                ('uid', models.CharField(help_text='学号', max_length=255, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('grade', models.CharField(blank=True, max_length=255, null=True, verbose_name='年级')),
                ('academy', models.CharField(blank=True, max_length=255, null=True, verbose_name='学院')),
                ('clazz', models.CharField(blank=True, max_length=255, null=True, verbose_name='班级')),
                ('credit', models.FloatField(blank=True, default=0, null=True, verbose_name='学时')),
                ('cxcy_credit', models.FloatField(blank=True, default=0, null=True, verbose_name='创新创业学时')),
                ('sxdd_credit', models.FloatField(blank=True, default=0, null=True, verbose_name='思想道德学时')),
                ('fl_credit', models.FloatField(blank=True, default=0, null=True, verbose_name='法律学时')),
                ('wt_credit', models.FloatField(blank=True, default=0, null=True, verbose_name='文体学时')),
                ('xl_credit', models.FloatField(blank=True, default=0, null=True, verbose_name='心理学时')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'student',
                'ordering': ('-credit',),
            },
        ),
    ]
