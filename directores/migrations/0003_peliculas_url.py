# Generated by Django 4.1 on 2022-08-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0002_alter_peliculas_dirigido_por_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='url',
            field=models.URLField(default='https://thelongfortgroup.com/public/img/default/no-image-icon.jpg'),
        ),
    ]
