# Generated by Django 2.0.3 on 2018-03-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0007_article_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Three',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_first', models.CharField(max_length=100)),
                ('text_first', models.TextField()),
                ('image_first', models.ImageField(blank=True, upload_to='')),
                ('title_second', models.CharField(max_length=100)),
                ('text_second', models.TextField()),
                ('image_second', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]