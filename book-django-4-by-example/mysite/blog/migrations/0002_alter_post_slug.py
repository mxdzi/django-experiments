# Generated by Django 4.2.9 on 2024-01-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="published"),
        )
    ]
