# Generated by Django 4.0.2 on 2022-02-04 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastMessege', models.CharField(max_length=50)),
                ('notification', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='store_image/')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('pin', models.BooleanField(default=False)),
                ('mute', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=15)),
            ],
        ),
    ]