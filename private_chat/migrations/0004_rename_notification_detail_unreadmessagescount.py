# Generated by Django 4.0.2 on 2022-02-09 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_chat', '0003_alter_detail_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='notification',
            new_name='unreadMessagesCount',
        ),
    ]