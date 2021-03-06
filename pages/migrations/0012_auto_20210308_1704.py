# Generated by Django 3.1.5 on 2021-03-08 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20210308_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='tweet_link',
        ),
        migrations.AddField(
            model_name='tip',
            name='tweet_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tip',
            name='posted_by',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tip',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
