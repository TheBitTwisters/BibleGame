# Generated by Django 2.1.3 on 2018-11-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20181121_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('M', 'Multiple Choice'), ('T', 'True or False'), ('S', 'Survey'), ('R', 'Survey Rush')], default='S', max_length=1),
        ),
    ]
