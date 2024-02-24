from django.db import models
from django.utils.translation import gettext as _

from project.utils.model_utils import BaseModel


class BusinessCenter(BaseModel):
    name = models.CharField(_("Business center name"), max_length=400)

    class Meta:
        db_table: str = "business_center"
        # db_table_comment: str = "" # Work with only PostgreSQL

        get_latest_by: str = "-update"
        ordering: tuple = ("-update",)

        verbose_name: str = _("Business center")
        verbose_name_plural: str = _("Business centers")

    def __str__(self) -> str:
        return "{id} - {name}".format(id=self.id, name=self.name)


class Floor(BaseModel):
    name = models.CharField(_("Floor name"), max_length=400)
    number = models.IntegerField(_("Floor number"))

    business_center = models.ForeignKey(BusinessCenter, on_delete=models.PROTECT)

    class Meta:
        db_table: str = "floors"
        # db_table_comment: str = "" # Work with only PostgreSQL

        get_latest_by: str = "-update"
        ordering: tuple = ("-update",)

        verbose_name: str = _("Floor")
        verbose_name_plural: str = _("Floors")

    def __str__(self) -> str:
        return "{id} - {businesscenter}:{name}:{number}".format(
            id=self.id,
            businesscenter=self.business_center,
            name=self.name,
            number=self.number
        )


class Office(BaseModel):
    name = models.CharField(_("Office name"), max_length=400)
    number = models.IntegerField(_("Office number"))

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name=_("Floor name"))

    class Meta:
        db_table: str = "offices"
        # db_table_comment: str = "" # Work with only PostgreSQL

        get_latest_by: str = "-update"
        ordering: tuple = ("-update",)

        verbose_name: str = _("Office")
        verbose_name_plural: str = _("Offices")

    def __str__(self) -> str:
        return "{id} - {name}:{number}".format(id=self.id, name=self.name, number=self.number)


class Door(BaseModel):
    name = models.CharField(_("Door name"), max_length=500)
    number = models.PositiveIntegerField(_("Door number"))

    office = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name=_("Office name"))

    class Meta:
        db_table: str = "doors"
        # db_table_comment: str = "" # Work with only PostgreSQL

        get_latest_by: str = "-update"
        ordering: tuple = ("-update",)

        verbose_name: str = _("Door")
        verbose_name_plural: str = _("Doors")

    def __str__(self) -> str:
        return "{id} - {name}:{number}".format(id=self.id, name=self.name, number=self.number)
