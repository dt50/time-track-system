from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import PROTECT, BooleanField, ForeignKey
from django.utils.translation import gettext as _
from model_utils import Choices
from model_utils.fields import StatusField

from project.organizations.models import Door
from project.utils.model_utils import BaseModel

User = get_user_model()


class TimeControl(BaseModel):
    STATUS = Choices(("IN", _("In")), ("OUT", _("Out")))

    user = ForeignKey(User, on_delete=PROTECT, verbose_name=_("User account"))

    status = StatusField(choices_name="STATUS", default=STATUS.IN, verbose_name=_("Status"))

    is_valid = BooleanField(_("Entry for counting"), default=True, help_text=_("Is the entry valid for counting"))

    door = ForeignKey(Door, on_delete=models.PROTECT)

    class Meta:
        db_table: str = "time_control"
        # db_table_comment: str = "" # Work with only PostgreSQL

        get_latest_by: str = "-update"
        ordering: tuple = ("-update",)

        verbose_name: str = _("Time control")
        verbose_name_plural: str = _("Time controls")

    def __str__(self) -> str:
        pass
