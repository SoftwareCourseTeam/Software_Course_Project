# Generated by Django 4.2.13 on 2024-06-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0006_borrow"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrow",
            name="status",
            field=models.BooleanField(default=0),
        ),
    ]