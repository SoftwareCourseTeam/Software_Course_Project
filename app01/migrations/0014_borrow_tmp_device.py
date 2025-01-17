# Generated by Django 4.2.13 on 2024-06-28 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0013_userinfo_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrow",
            name="tmp_device",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tmp_devices",
                to="app01.device",
            ),
        ),
    ]
