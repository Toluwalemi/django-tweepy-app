# Generated by Django 3.1.5 on 2021-03-04 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210304_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='media_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
