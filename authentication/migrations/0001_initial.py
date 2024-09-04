# Generated by Django 5.1.1 on 2024-09-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PortalUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
