# Generated by Django 2.0.3 on 2018-03-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0003_auto_20180325_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_one',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
