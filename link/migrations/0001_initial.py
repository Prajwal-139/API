# Generated by Django 4.1.8 on 2023-04-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookMyShow",
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
                ("Mname", models.CharField(max_length=20)),
                ("Mtime", models.TimeField()),
                ("Mdate", models.DateField()),
                ("Mticket", models.FloatField()),
                ("Popcorn", models.BooleanField(default=False)),
            ],
        ),
    ]
