# Generated by Django 4.1.5 on 2023-02-06 08:25

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_usermodel_firstname_remove_usermodel_lastname_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]