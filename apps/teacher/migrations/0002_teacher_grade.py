# Generated by Django 4.2.2 on 2023-06-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="grade",
            field=models.CharField(default=1, max_length=50, verbose_name="Класс"),
            preserve_default=False,
        ),
    ]
