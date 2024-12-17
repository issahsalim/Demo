# Generated by Django 5.0.1 on 2024-08-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='absenceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_indexNumber', models.CharField(max_length=10)),
                ('reason', models.TextField()),
                ('proveFile', models.FileField(blank=True, null=True, upload_to='upload')),
                ('submitted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Assess_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_Number', models.CharField(max_length=10)),
                ('Total_Quiz_Marks', models.FloatField()),
                ('Total_Assignment_Mark', models.FloatField()),
                ('Attendance_Mark', models.FloatField()),
                ('Mid_Sem', models.FloatField()),
                ('Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='staticIndexNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_IndexNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='studentLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('indexnumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='studentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_number', models.CharField(max_length=10)),
                ('Quizzes', models.IntegerField(default=0, editable=False)),
                ('Assignments', models.IntegerField(default=0, editable=False)),
            ],
        ),
    ]
