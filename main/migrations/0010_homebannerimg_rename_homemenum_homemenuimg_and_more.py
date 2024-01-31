# Generated by Django 4.2.3 on 2024-01-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_rename_homebannerimg_homebannerm_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeBannerImg",
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
                ("banner_name", models.CharField(max_length=20)),
                ("content", models.CharField(max_length=30, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="banner")),
            ],
        ),
        migrations.RenameModel(
            old_name="HomeMenuM",
            new_name="HomeMenuImg",
        ),
        migrations.DeleteModel(
            name="HomeBannerM",
        ),
        migrations.RenameField(
            model_name="homemenuimg",
            old_name="title",
            new_name="menu_name",
        ),
    ]
