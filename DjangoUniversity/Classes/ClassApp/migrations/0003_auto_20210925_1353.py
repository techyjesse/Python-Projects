# Generated by Django 3.2.7 on 2021-09-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassApp', '0002_rename_duration_djangoclasses_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoclasses',
            name='course_Number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='djangoclasses',
            name='instructor_Name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]