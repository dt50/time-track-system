# Generated by Django 5.0.1 on 2024-02-23 17:40

import django.db.models.deletion
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeControl",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "create",
                    models.DateTimeField(
                        blank=True, help_text="Timestamp of object create", verbose_name="Create time"
                    ),
                ),
                (
                    "update",
                    models.DateTimeField(
                        blank=True, help_text="Timestamp of object update", verbose_name="Update time"
                    ),
                ),
                (
                    "status",
                    model_utils.fields.StatusField(
                        choices=[("IN", "In"), ("OUT", "Out")],
                        default="IN",
                        max_length=100,
                        no_check_for_status=True,
                        verbose_name="Status",
                    ),
                ),
                (
                    "is_valid",
                    models.BooleanField(
                        default=True, help_text="Is the entry valid for counting", verbose_name="Entry for counting"
                    ),
                ),
                ("door", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="organizations.door")),
            ],
            options={
                "verbose_name": "Time control",
                "verbose_name_plural": "Time controls",
                "db_table": "time_control",
                "ordering": ("-update",),
                "get_latest_by": "-update",
            },
        ),
    ]
