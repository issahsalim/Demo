# Generated by Django 5.1.1 on 2024-11-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessementApp', '0004_headmaster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absencereport',
            name='stu_indexNumber',
        ),
        migrations.AddField(
            model_name='absencereport',
            name='Parent_Name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='absencereport',
            name='Student_Class',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='absencereport',
            name='Student_Name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
