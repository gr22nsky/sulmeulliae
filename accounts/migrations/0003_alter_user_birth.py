# Generated by Django 4.2 on 2024-09-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
