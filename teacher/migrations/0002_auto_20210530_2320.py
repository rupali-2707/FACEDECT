# Generated by Django 3.2 on 2021-05-30 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='status',
        ),
    ]