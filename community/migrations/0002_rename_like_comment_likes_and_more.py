# Generated by Django 4.2 on 2024-10-08 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="like",
            new_name="likes",
        ),
        migrations.RenameField(
            model_name="community",
            old_name="like",
            new_name="likes",
        ),
    ]