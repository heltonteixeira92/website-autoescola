# Generated by Django 3.2.5 on 2021-08-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postagem_fonte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='fonte',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
