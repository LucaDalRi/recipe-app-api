"""
wait for db avaible
"""
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
import time

from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Databse unavaible, waiting 1 sec')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))