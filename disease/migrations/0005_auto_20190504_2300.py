# Generated by Django 2.2.1 on 2019-05-04 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_auto_20190504_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['name'], 'verbose_name': 'Disease'},
        ),
    ]
