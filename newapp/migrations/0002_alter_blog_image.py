# Generated by Django 4.1.1 on 2022-09-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
