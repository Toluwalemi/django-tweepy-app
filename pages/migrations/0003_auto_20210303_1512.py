# Generated by Django 3.1.5 on 2021-03-03 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210303_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='pages.tip'),
        ),
    ]
