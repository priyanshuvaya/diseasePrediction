# Generated by Django 2.2.1 on 2019-05-04 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
