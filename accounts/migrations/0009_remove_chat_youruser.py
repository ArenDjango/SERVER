# Generated by Django 2.0.3 on 2018-04-26 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_chat_youruser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='youruser',
        ),
    ]
