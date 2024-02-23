from io import StringIO

from django.core.management.base import BaseCommand

from project.utils.ascii_art import DSOL


class AdditionalCommand(BaseCommand):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def print_logo(self):
        self.stdout.write(DSOL, ending="\n\n")
