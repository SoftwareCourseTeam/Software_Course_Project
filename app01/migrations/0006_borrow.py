# Generated by Django 4.2.13 on 2024-06-27 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0005_alter_device_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Borrow",
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
                ("number", models.PositiveIntegerField()),
                ("borrow_date", models.DateTimeField(auto_now_add=True)),
                ("return_date", models.DateTimeField(blank=True, null=True)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.device"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.userinfo"
                    ),
                ),
            ],
        ),
    ]
