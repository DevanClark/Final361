# Generated by Django 2.2 on 2019-04-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0003_auto_20190402_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.CharField(max_length=50)),
                ('startTime', models.CharField(max_length=50)),
                ('endTime', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='pa',
        ),
    ]
