# Generated by Django 3.2.5 on 2021-07-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='fonte',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='img',
            field=models.ImageField(upload_to='blog_img'),
        ),
    ]