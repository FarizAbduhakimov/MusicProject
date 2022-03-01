# Generated by Django 4.0.1 on 2022-02-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_album_url_alter_album_description_alter_album_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-time_create'], 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['-time_create'], 'verbose_name': 'Artist, lyricist and composer', 'verbose_name_plural': 'Artists'},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['-time_create'], 'verbose_name': 'Music', 'verbose_name_plural': 'Musics'},
        ),
        migrations.AddField(
            model_name='album',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
