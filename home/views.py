from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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

    def dispatch(self, request, *args, **kwargs):
        # Vérifier si l'utilisateur est authentifié
        if request.user.is_authenticated:
            # Rediriger vers le tableau de bord
            return redirect(
                reverse_lazy('dashboard'))  # Remplacez 'dashboard' par le nom correct de votre URL de tableau de bord
        # Si non authentifié, continuer vers la page d'accueil
        return super().dispatch(request, *args, **kwargs)