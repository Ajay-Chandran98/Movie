# Generated by Django 4.1 on 2024-05-16 10:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("film", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Movie",
            new_name="Film",
        ),
    ]
