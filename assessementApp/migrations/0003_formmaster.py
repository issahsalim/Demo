# Generated by Django 5.1.1 on 2024-11-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessementApp', '0002_alter_assess_student_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ClassHanlder', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField(max_length=10)),
                ('age', models.IntegerField()),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
