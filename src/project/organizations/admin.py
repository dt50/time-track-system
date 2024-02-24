from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from .models import BusinessCenter, Door, Floor, Office


@admin.register(BusinessCenter)
class FloorAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    fieldsets: tuple = (
        (
            None,
            {"fields": ("name",)},
        ),
    )

    list_display: tuple = ("name",)
    list_filter: tuple = ("name", "update")

    list_per_page: int = 50

    search_fields: tuple = ("name",)


@admin.register(Floor)
class FloorAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    fieldsets: tuple = (
        (
            None,
            {"fields": ("business_center", "name", "number")},
        ),
    )

    list_display: tuple = ("business_center", "name", "number")
    list_filter: tuple = ("business_center__name", "name", "number", "update")

    list_per_page: int = 50

    search_fields: tuple = ("business_center__name", "name", "number")


@admin.register(Office)
class OfficeAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    fieldsets: tuple = (
        (
            None,
            {"fields": ("name", "number", "floor")},
        ),
    )

    list_display: tuple = ("name", "number", "floor")
    list_filter: tuple = ("name", "number", "floor__name", "update")

    list_per_page: int = 50

    search_fields: tuple = ("name", "number", "floor__name")


@admin.register(Door)
class DoorAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    fieldsets: tuple = (
        (
            None,
            {"fields": ("name", "number", "office")},
        ),
    )

    list_display: tuple = ("name", "number", "office")
    list_filter: tuple = ("name", "number", "office__name", "update")

    list_per_page: int = 50

    search_fields: tuple = ("name", "number", "office__name")
