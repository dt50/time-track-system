from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    create = models.DateTimeField(_("Create time"), help_text=_("Timestamp of object create"), blank=True)
    update = models.DateTimeField(_("Update time"), help_text=_("Timestamp of object update"), blank=True)

    objects = models.Manager()
    objects_bulk = BulkUpdateOrCreateQuerySet.as_manager()

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, *args, **kwargs) -> None:
        if self.id:
            self.update = timezone.now()
        else:
            self.create = timezone.now()
            self.update = timezone.now()

        super().save(*args, **kwargs)
