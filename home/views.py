from django.shortcuts import render
from django.views.generic import ListView

from feeds.models import RSSFeed
from publications.models import Publication  # Assurez-vous que le modèle Publication est importé


class HomeView(ListView):
    model = RSSFeed
    template_name = 'home/home.html'
    context_object_name = 'rss_feeds'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publications'] = Publication.objects.all()  # Ajoutez les publications au contexte
        return context
