# Generated by Django 4.1.1 on 2022-09-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
