# Generated by Django 4.0.4 on 2022-06-15 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_document_writter_alter_music_username_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='username',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
    ]
