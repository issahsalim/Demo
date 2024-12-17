# Generated by Django 5.1.1 on 2024-11-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessementApp', '0003_formmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
