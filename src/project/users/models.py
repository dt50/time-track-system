from django.contrib.auth.models import AbstractUser
# from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db.models import CharField, EmailField, Index, ManyToManyField
# from django.db.models.functions import Upper
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from project.users.managers import UserManager
from project.utils.model_utils import BaseModel


class User(AbstractUser):
    """
    Default custom user model for project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First name of User"), blank=True, max_length=255)
    last_name = CharField(_("Last name of User"), blank=True, max_length=255)
    email = EmailField(_("email address"), unique=True)
    username = CharField(_("User name of User"), blank=True, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    # class Meta:
    #     indexes = [
    #         Index(Upper("name"), name="name_upper_index"),
    #         GinIndex(
    #             fields=["first_name", "last_name"], name="name_gin_index", opclasses=["gin_trgm_ops", "gin_trgm_ops"]
    #         ),
    #         GinIndex(OpClass(Upper("first_name"), name="gin_trgm_ops"), name="first_name_upper_gin_index"),
    #         GinIndex(OpClass(Upper("last_name"), name="gin_trgm_ops"), name="last_name_upper_gin_index"),
    #     ]

    def __str__(self):
        return self.email

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"pk": self.id})
