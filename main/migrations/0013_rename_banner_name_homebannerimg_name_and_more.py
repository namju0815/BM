# Generated by Django 4.2.3 on 2024-01-17 16:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_rename_storename_store_name_remove_store_foodimg_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="homebannerimg",
            old_name="banner_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="homemenuimg",
            old_name="menu_name",
            new_name="name",
        ),
    ]
