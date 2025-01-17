# Generated by Django 4.2.13 on 2024-06-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_device"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="model_spec",
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="device",
            name="purchase_date",
            field=models.DateField(blank=True, default=None, max_length=32, null=True),
        ),
    ]
