from django.conf import settings
from django.core.management.base import BaseCommand

from tests.models import DjangoNewsIssue


class Command(BaseCommand):
    help = "Creates initial objects for the site"

    def handle(self, *args, **options):
        self.stdout.write("Creating objects...")

        # Django News scraping (sorry William and Jeff)
        last_issue = DjangoNewsIssue.objects.last()
        if last_issue:
            issue = DjangoNewsIssue.objects.create()
            issue.scrap_data()
