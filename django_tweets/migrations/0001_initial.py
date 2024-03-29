# Generated by Django 4.2.4 on 2023-08-28 15:41

from django.db import migrations, models
import django.db.models.deletion
import django_tweets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='Title')),
                ('file', models.FileField(upload_to=django_tweets.models._upload_path, verbose_name='File')),
                ('upload', models.BooleanField(default=True, verbose_name='Upload to Twitter')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('expires_at', models.DateTimeField(blank=True, null=True, verbose_name='Expires at')),
                ('media_id_string', models.CharField(blank=True, editable=False, max_length=32, null=True)),
                ('response', models.TextField(blank=True, null=True, verbose_name='Tweepy Response')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=4096)),
                ('id_string', models.CharField(blank=True, editable=False, max_length=32)),
                ('edit_history_tweet_ids', models.TextField(blank=True, editable=False, max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('response', models.TextField(blank=True, null=True, verbose_name='Tweepy Response')),
                ('files', models.ManyToManyField(blank=True, to='django_tweets.mediafile')),
            ],
        ),
        migrations.CreateModel(
            name='TweetPublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=False)),
                ('tweet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_tweets.tweet')),
            ],
        ),
    ]
