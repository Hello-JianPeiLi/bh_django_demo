# Generated by Django 3.2.6 on 2021-08-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_auto_20210807_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bcomment',
            field=models.IntegerField(default=0),
        ),
    ]
