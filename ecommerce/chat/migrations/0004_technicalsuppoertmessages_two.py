# Generated by Django 2.1.7 on 2019-05-17 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_technicalsuppoertmessages_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalsuppoertmessages',
            name='two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='two', to=settings.AUTH_USER_MODEL),
        ),
    ]
