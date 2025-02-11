# Generated by Django 4.1 on 2024-05-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movies",
            old_name="GENRE",
            new_name="CATEGORY",
        ),
        migrations.RenameField(
            model_name="movies",
            old_name="image_card",
            new_name="POSTER",
        ),
        migrations.RemoveField(
            model_name="movies",
            name="image_cover",
        ),
        migrations.RemoveField(
            model_name="movies",
            name="length",
        ),
        migrations.RemoveField(
            model_name="movies",
            name="movie_views",
        ),
        migrations.AddField(
            model_name="movies",
            name="YOUTUBE_TRAILER",
            field=models.URLField(blank=True, null=True),
        ),
    ]
