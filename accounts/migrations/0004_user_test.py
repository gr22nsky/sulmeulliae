# Generated by Django 4.2 on 2024-09-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_user_birth_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="test",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]