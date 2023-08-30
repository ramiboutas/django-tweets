from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import Q


from django_tweets.models import Tweet
from tests.models import DjangoNewsIssueItem


class Command(BaseCommand):
    help = "Publishes a Tweet object"

    def handle(self, *args, **options):
        self.stdout.write("Publishing tweet...")
        issue_items = DjangoNewsIssueItem.objects.filter(
            Q(category="Articles") | Q(category="Tutorials")
        )
        tweets = []
        for item in issue_items:
            tweets.append(
                Tweet(
                    text=f"[Post from Django News]\n\n{item.title}\n\n{item.text}\n\n{item.url}"
                )
            )
        Tweet.objects.bulk_create(tweets)

        self.stdout.write("Done!")
