# Generated by Django 3.1.4 on 2021-08-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0010_auto_20210812_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictest',
            name='pic_name',
            field=models.CharField(default='null', max_length=20, unique=True),
        ),
    ]