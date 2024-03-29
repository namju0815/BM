# Generated by Django 4.2.3 on 2024-01-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0015_dishescategory_store_dishes_categories"),
    ]

    operations = [
        migrations.DeleteModel(
            name="HomeMenuImg",
        ),
        migrations.AddField(
            model_name="dishescategory",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="homeMenu"),
        ),
        migrations.AlterField(
            model_name="dishescategory",
            name="name",
            field=models.CharField(max_length=20),
        ),
    ]
