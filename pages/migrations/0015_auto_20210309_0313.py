# Generated by Django 3.1.5 on 2021-03-09 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20210309_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='daily_tip',
            field=models.CharField(max_length=140, unique=True),
        ),
    ]
