import time

from django.test import TestCase
from django.utils import timezone

from django_tweets.models import Tweet
from django_tweets.clients import get_v2_client


now = timezone.now()
now_tupple_6 = (now.year, now.month, now.day, now.hour, now.minute, now.second)


class TweetModelTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_create_and_delete_tweet(self):
        text = "%s-%s-%s %s:%s:%s Testing django-tweets." % now_tupple_6
        tweet = Tweet.objects.create(text=text)
        published_tweet = tweet.publish()
        time.sleep(2)
        published_tweet.delete()
