# Generated by Django 2.2.13 on 2020-06-11 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200611_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]