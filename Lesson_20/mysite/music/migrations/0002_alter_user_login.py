# Generated by Django 4.1.5 on 2023-01-08 19:27

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="login",
            field=models.CharField(
                max_length=100, null=True, validators=[music.models.validate_login]
            ),
        ),
    ]
