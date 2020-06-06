from django.core.management import BaseCommand
from django.db import connection
from django.db.utils import OperationalError
from django.utils.translation import gettext_lazy as _
import time

class Command(BaseCommand):
    help = "Checks if the Database is ready to accept connections."

    def handle(self, *args, **options):
        self.stdout.write(self.style.ERROR(_("Waiting for Database to accept connections.")))
        conn = None

        while not conn:
            try:
                connection.ensure_connection()
                conn = True
            except OperationalError:
                self.stdout.write(self.style.ERROR(_("Database not available. Will retry after 1 second.")))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS(_("Database ready to accept connections!")))