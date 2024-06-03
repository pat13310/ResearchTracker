from __future__ import absolute_import, unicode_literals
from celery import shared_task
from feeds.models import RSSFeed
import requests


@shared_task
def fetch_rss_feed(feed_id):
    feed = RSSFeed.objects.get(id=feed_id)
    response = requests.get(feed.url)
    if response.status_code == 200:
        feed.description = response.text[:255]  # Simplified example
        feed.save()
    return 'RSS feed updated'


@shared_task
def update_all_feeds():
    feeds = RSSFeed.objects.all()
    for feed in feeds:
        fetch_rss_feed.delay(feed.id)
    return 'All feeds updated'


@shared_task(bind=True)
def test_task():
    print("Celery is working!")
    return 'Test: Tâche exécutée'
