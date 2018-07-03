# Generated by Django 2.0.3 on 2018-04-26 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='youruser',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='youruser', to=settings.AUTH_USER_MODEL),
        ),
    ]