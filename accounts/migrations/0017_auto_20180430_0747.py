# Generated by Django 2.0.3 on 2018-04-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_photo_orphotoorvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='orphotoorvideo',
            field=models.BooleanField(default=False),
        ),
    ]
