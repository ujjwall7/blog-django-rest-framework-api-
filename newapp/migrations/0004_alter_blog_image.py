# Generated by Django 4.1.1 on 2022-09-29 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.FileField(upload_to='media'),
        ),
    ]
