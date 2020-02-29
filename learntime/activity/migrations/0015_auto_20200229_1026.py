# Generated by Django 2.2.6 on 2020-02-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0014_auto_20200228_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='credit_type',
            field=models.CharField(blank=True, choices=[('fl_credit', '法律'), ('wt_credit', '文体'), ('xl_credit', '心理'), ('cxcy_credit', '创新创业'), ('sxdd_credit', '思想道德')], default='n', max_length=20, null=True, verbose_name='学时类别'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=255, verbose_name='活动名称'),
        ),
    ]
