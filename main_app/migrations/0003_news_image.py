# Generated by Django 4.1.3 on 2022-12-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_news_title_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]