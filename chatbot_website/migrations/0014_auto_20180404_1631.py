# Generated by Django 2.0.3 on 2018-04-04 10:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0013_remove_article_fourth_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_one',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='article_three',
            name='image_second',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='article_two',
            name='image_third',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
