# Generated by Django 2.0.2 on 2018-03-29 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogbreeds', '0002_auto_20180329_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogbreed',
            name='drools',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dogbreed',
            name='goodWC',
            field=models.CharField(max_length=200),
        ),
    ]
