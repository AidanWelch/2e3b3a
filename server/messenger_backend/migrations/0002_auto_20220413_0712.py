# Generated by Django 3.2.4 on 2022-04-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='user1Unread',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='conversation',
            name='user2Unread',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]