# Generated by Django 4.2.3 on 2024-01-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_customuser"),
    ]

    operations = [
        migrations.RenameField(
            model_name="store",
            old_name="storename",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="store",
            name="foodimg",
        ),
        migrations.AddField(
            model_name="store",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="store"),
        ),
    ]
