# Generated by Django 2.2.13 on 2020-06-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('permission', models.CharField(choices=[('normal', 'normal user'), ('super', 'super user')], max_length=1)),
            ],
        ),
    ]