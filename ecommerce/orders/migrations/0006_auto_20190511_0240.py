# Generated by Django 2.1.7 on 2019-05-11 00:40

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190511_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
