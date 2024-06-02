from django.contrib.syndication.views import Feed
from django.urls import reverse
from publications.models import Publication


class LatestPublicationsFeed(Feed):
    title = "Latest Publications"
    link = "/rss/"
    description = "Updates on the latest publications."

    def items(self):
        return Publication.objects.order_by('-publication_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.authors

    def item_link(self, item):
        return reverse('publication-detail', args=[item.pk])
