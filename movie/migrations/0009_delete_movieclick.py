# Generated by Django 4.1 on 2024-05-20 11:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0008_movieclick"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MovieClick",
        ),
    ]