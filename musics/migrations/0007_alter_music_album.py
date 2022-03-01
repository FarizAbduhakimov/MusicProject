# Generated by Django 4.0.1 on 2022-02-03 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0006_alter_music_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musics.album'),
        ),
    ]
