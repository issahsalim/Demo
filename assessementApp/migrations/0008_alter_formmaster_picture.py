# Generated by Django 5.1.1 on 2024-11-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessementApp', '0007_alter_headmaster_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmaster',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]