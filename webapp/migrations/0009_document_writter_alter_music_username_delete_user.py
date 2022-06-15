# Generated by Django 4.0.4 on 2022-06-15 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0008_alter_document_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='writter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='music',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]