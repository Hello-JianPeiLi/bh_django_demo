# Generated by Django 3.1.4 on 2021-08-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0007_auto_20210810_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='booktest/media')),
            ],
        ),
    ]
