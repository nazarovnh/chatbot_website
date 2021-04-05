# Generated by Django 2.0.3 on 2021-04-05 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0021_auto_20210308_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article_one',
            options={'ordering': ['title'], 'verbose_name': 'Статья тип 1', 'verbose_name_plural': 'Статья тип 1'},
        ),
        migrations.AlterField(
            model_name='article_one',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='article_one',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='chatbot_website.Category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]