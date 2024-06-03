import feedparser
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import RSSFeed
from .forms import RSSFeedForm


class RSSFeedListView(ListView):
    model = RSSFeed
    template_name = 'feeds/rssfeed_list.html'
    context_object_name = 'rss_feeds'


class RSSFeedCreateView(CreateView):
    model = RSSFeed
    form_class = RSSFeedForm
    template_name = 'feeds/rssfeed_form.html'
    success_url = reverse_lazy('rss-feed-list')


class RSSFeedUpdateView(UpdateView):
    model = RSSFeed
    form_class = RSSFeedForm
    template_name = 'feeds/rssfeed_form.html'
    success_url = reverse_lazy('rss-feed-list')


class RSSFeedDeleteView(DeleteView):
    model = RSSFeed
    template_name = 'feeds/rssfeed_confirm_delete.html'
    success_url = reverse_lazy('rss-feed-list')


class RSSFeedDetailView(DetailView):
    model = RSSFeed
    template_name = 'feeds/rss_feed_detail.html'
    context_object_name = 'feed'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feed = self.get_object()
        parsed_feed = feedparser.parse(feed.url)
        context['entries'] = parsed_feed.entries
        return context