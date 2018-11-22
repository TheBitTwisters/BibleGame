# Generated by Django 2.1.3 on 2018-11-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_choice_mark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='play_choice',
        ),
        migrations.RemoveField(
            model_name='game',
            name='play_refresh',
        ),
        migrations.AddField(
            model_name='game',
            name='play_modal',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]