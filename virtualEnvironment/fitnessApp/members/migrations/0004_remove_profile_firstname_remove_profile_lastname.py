# Generated by Django 5.0.4 on 2024-06-23 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_member_lastname_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
    ]