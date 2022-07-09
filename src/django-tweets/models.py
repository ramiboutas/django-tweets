from django.db import models



class Tweet(models.Model):
    created_at      = models.DateTimeField()
    favorite_count  = models.IntegerField()
    twitter_id      = models.IntegerField()
    id_str          = models.CharField(max_length=30)
    retweet_count   = models.IntegerField()
    text            = models.TextField(max_length=280)
    
    twitter_url     = models.URLField(null=True)
    
    def __str__(self) -> str:
        return self.text
    
    def save(self, *args, **kwargs):
        self.twitter_url = f"https://twitter.com/{TWIITER_USERNAME}/status/{self.id_str}"
        super(Tweet, self).save(*args, **kwargs)
