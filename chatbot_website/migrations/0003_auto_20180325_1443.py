# Generated by Django 2.0.3 on 2018-03-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0002_auto_20180325_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_first', models.CharField(max_length=100)),
                ('text_first', models.TextField()),
                ('image_first', models.ImageField(blank=True, upload_to='vk/')),
                ('title_second', models.CharField(max_length=100)),
                ('text_second', models.TextField()),
                ('image_second', models.ImageField(blank=True, upload_to='telegram/')),
                ('title_third', models.CharField(max_length=100)),
                ('text_third', models.TextField()),
                ('image_third', models.ImageField(blank=True, upload_to='messenger/')),
            ],
        ),
        migrations.AlterField(
            model_name='article_one',
            name='image',
            field=models.ImageField(blank=True, upload_to='one/'),
        ),
    ]