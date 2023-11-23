from django.core.management.base import BaseCommand
import pendulum
import pprint

"""
    This management tool (MT) takes in an article that has been manually marked up and parses and breaks down the logic
    into database tables (database brd_pending). There is no attempt to populate the tables with actual foreign keys -
    that will be done by another MT.
"""

class Command(BaseCommand):
    help = "Read in data from a markup text file and parse it and break down the logic, populating work tables"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update database. Default is to reset database.",
        )

    def handle(self, *args, **kwargs):
        debug = False
