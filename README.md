# django-tweets
Create and delete tweets in a Django project.

This packages takes the advantage of the [tweepy](https://www.tweepy.org/) functionalies to connect it to a Django Backend.

The tweets objects can have media files as well.


## Set up


### Twitter Account

1. Make sure you have a Twitter account.
2. Go to the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard).
3. Create a Project and an App
4. Make sure your App has read and write permissions.
5. Genenerate the necessary secrets and token.


### django-tweets


1. Install from PyPI
```
python -m pip install django-tweets
```

2. Add the package to your settins INSTALLED_APPS

```python

INSTALLED_APPS = [
    ...
    "django_tweets",
    ...
]

```




3. Add the following settings to your Django project.

| Django setting              | Description                                                                 | Required |
|-----------------------------|-----------------------------------------------------------------------------|----------|
| TWITTER_API_KEY             | Twitter API OAuth 1.0a Consumer Key                                         | Yes      |
| TWITTER_API_KEY_SECRET      | Twitter API OAuth 1.0a Consumer Secret                                      | Yes      |
| TWITTER_BEARER_TOKEN        | Twitter API OAuth 2.0 Bearer Token / Access Token                           | Yes      |
| TWITTER_ACCESS_TOKEN        | Twitter API OAuth 1.0a Access Token                                         | Yes      |
| TWITTER_ACCESS_TOKEN_SECRET | Twitter API OAuth 1.0a Access Token Secret                                  | Yes      |
| DJANGO_TWEETS_SYNC_DELETE   | Synchronize object deletion with Twitter API. This is activated by default. | No       |



Example:

```python
import os
from dotenv import load_dotenv
load_dotenv()

...

# django-tweets
# Consumer Keys
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_KEY_SECRET = os.environ.get("TWITTER_API_KEY_SECRET")
# Authentication Tokens
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
# OAuth 2.0 Client ID and Client Secret
TWITTER_CLIENT_ID = os.environ.get("TWITTER_CLIENT_ID")
TWITTER_CLIENT_SECRET = os.environ.get("TWITTER_CLIENT_SECRET")

```


4. Run migrations

```
python manage.py migrate

```



## Usage


### Create a simple tweet

```python

from django_tweets.models import Tweet

# create a tweet in the db
tweet = Tweet.objects.create(text="Hi, this is my tweet using django-tweets and tweepy")

# publish it
tweet.publish()

```
### Create a simple tweet with a media file

```python
from pathlib import Path
from django.core.files import File
from django_tweets.models import Tweet, MediaFile

# create a media file
path = Path("path/to/my/file.jpg")
with path.open(mode="rb") as f:
    mediafile = MediaFile.objects.create(
      title="nice photo",
      file=File(f, name=path.name)
    )

# create a tweet in the db
tweet = Tweet.objects.create(text="Hi, this is my tweet using django-tweets and tweepy")

## add the media file to the tweet object
tweet.files.add(mediafile)

# publish it
tweet.publish()

```





## Questions
* How Can I get the read and write permission for my app?
Answer:
1. In the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard), click on gear icon of the project app

![Gear icon app settings](images/app_settings.png)


2. Then go _User authentication settings_ and click on the _Edit_ button.

![Edit user auth settings](images/edit_permissions.png)


3. Configure the the form and submit.

![User authentication settings](images/app_user_permissions.png)









## About



©Django is a registered trademark of the Django Software Foundation.
