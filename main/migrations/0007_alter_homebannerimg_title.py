# Generated by Django 4.2.3 on 2024-01-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_homebannerimg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homebannerimg",
            name="title",
            field=models.CharField(default="dlfeks", max_length=20),
            preserve_default=False,
        ),
    ]
