# Generated by Django 2.1.1 on 2018-11-23 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_team_buzz_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='points',
            new_name='fails',
        ),
    ]
