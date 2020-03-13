# Generated by Django 2.2.6 on 2020-01-18 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_studentactivity_credit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentactivity',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='join_students', to='activity.Activity', verbose_name='活动'),
        ),
    ]
