# Generated by Django 2.2 on 2019-04-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0004_auto_20190422_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='studentsInCourse',
        ),
        migrations.AddField(
            model_name='user',
            name='myCourses',
            field=models.ManyToManyField(to='Final.Course'),
        ),
    ]