# Generated by Django 2.2.10 on 2020-05-03 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]