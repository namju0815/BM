# Generated by Django 4.2.3 on 2024-01-17 05:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_homemenuimg_alter_homebannerimg_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="HomeBannerImg",
            new_name="HomeBannerM",
        ),
        migrations.RenameModel(
            old_name="HomeMenuImg",
            new_name="HomeMenuM",
        ),
    ]