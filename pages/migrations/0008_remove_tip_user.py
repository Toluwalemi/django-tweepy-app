# Generated by Django 3.1.5 on 2021-03-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_link_media_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tip',
            name='user',
        ),
    ]
