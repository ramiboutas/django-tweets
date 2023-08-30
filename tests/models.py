from datetime import datetime

import requests
from bs4 import BeautifulSoup

import auto_prefetch

from django.db import models
from django.utils.functional import cached_property


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.3"
}


class DjangoNewsIssue(models.Model):
    title = models.CharField(max_length=128, null=True)
    date = models.DateField(null=True)

    @cached_property
    def url(self):
        return "https://django-news.com/issues/%s" % self.id

    def scrap_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            self.title = soup.title.text
            str_date = soup.select("time.published")[0]["datetime"]
            self.date = datetime.strptime(str_date, "%Y-%m-%d").date()
            self.save()
            # get items
            h3_titles = soup.select("h3.item__title")
            issue_items = []
            for h3_title in h3_titles:
                issue_items.append(
                    DjangoNewsIssueItem(
                        issue=self,
                        title=h3_title.text,
                        text=h3_title.find_next("p").text,
                        url=h3_title.find_next("a")["href"],
                        category=h3_title.parent.parent.find("h2").text,
                    )
                )
            DjangoNewsIssueItem.objects.bulk_create(issue_items)
        except Exception as e:
            self.delete()

    def __str__(self):
        return self.title


class DjangoNewsIssueItem(auto_prefetch.Model):
    issue = models.ForeignKey(DjangoNewsIssue, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=128, null=True)
    text = models.TextField(max_length=2096, null=True)
    url = models.CharField(max_length=128, null=True)
    category = models.CharField(max_length=32, null=True)

    class Meta(auto_prefetch.Model.Meta):
        pass

    def __str__(self):
        return "%s (%s)" % (self.title, self.issue.title)
