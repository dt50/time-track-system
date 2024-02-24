from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from .models import TimeControl


@admin.register(TimeControl)
class TimeControlAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    fieldsets: tuple = (
        (
            None,
            {"fields": ("user", "status", "door", "is_valid")},
        ),
    )

    list_display: tuple = ("user", "status", "is_valid", "door")
    list_filter: tuple = (
        "user__first_name",
        "user__last_name",
        "status",
        "door__number",
        "door__office__number",
        "door__office__floor__number",
        "update",
    )

    list_per_page: int = 50

    search_fields: tuple = (
        "user",
        "status",
        "door",
    )
