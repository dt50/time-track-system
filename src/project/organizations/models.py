from django.utils.translation import gettext as _
from project.utils.model_utils import BaseModel
from django.db import models


class Floor(BaseModel):
    name = models.CharField(_("Floor name"), max_length=400)
    number = models.IntegerField(_("Floor number"))

    class Meta:
        db_table: str = "floors"
        # db_table_comment: str = "" # Work with only PostgreSQL

        get_latest_by: str = "-update"
        ordering: tuple = ("-update",)

        verbose_name: str = _("Floor")
        verbose_name_plural: str = _("Floors")

    def __str__(self) -> str:
        return "{id} - {name}:{number}".format(id=self.id, name=self.name, number=self.number)


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
    number = models.PositiveIntegerField(_("Door number"), primary_key=True)

    office = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name=_("Office name"))

    class Meta:
        db_table: str = "doors"
        # db_table_comment: str = "" # Work with only PostgreSQL

        get_latest_by: str = "-update"
        ordering: tuple = ("-update",)

        verbose_name: str = _("Door data")
        verbose_name_plural: str = _("Doors data")

    def __str__(self) -> str:
        return "{id} - {name}:{number}".format(id=self.id, name=self.name, number=self.number)
