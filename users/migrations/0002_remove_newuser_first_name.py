# Generated by Django 4.0.2 on 2022-02-21 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='first_name',
        ),
    ]