# Generated by Django 2.2.6 on 2019-11-12 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_logs', to=settings.AUTH_USER_MODEL, verbose_name='操作者')),
            ],
            options={
                'verbose_name': '日志',
                'verbose_name_plural': '日志',
                'db_table': 'log',
                'ordering': ('-created_at',),
            },
        ),
    ]
