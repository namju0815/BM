# Generated by Django 4.2.3 on 2024-01-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_store_foodimg"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="comment",
            field=models.CharField(default="Your Default Comment", max_length=30),
            preserve_default=False,
        ),
    ]
