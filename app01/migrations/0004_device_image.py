# Generated by Django 4.2.13 on 2024-06-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0003_device_model_spec_device_purchase_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="image",
            field=models.BinaryField(null=True),
        ),
    ]