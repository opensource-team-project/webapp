# Generated by Django 4.0.4 on 2022-06-15 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_registereduser_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registereduser',
            new_name='User',
        ),
    ]
