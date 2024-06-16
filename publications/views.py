from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from rest_framework import viewsets

from .models import Publication, PublicationVersion
from .forms import PublicationForm, PublicationVersionForm
from serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Publication
from django.db.models import Q


class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'publications/publication_list.html'
    context_object_name = 'publications'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        queryset = Publication.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        search_by = self.request.GET.get('search_by', 'title')
        if query:
            if search_by == 'title':
                queryset = queryset.filter(title__icontains=query)
            elif search_by == 'date':
                queryset = queryset.filter(publication_date__icontains=query)
        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context['publications'])
        else:
            return super().render_to_response(context, **response_kwargs)

    def render_to_json_response(self, queryset):
        publications = list(queryset.values())
        return JsonResponse(publications, safe=False)


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publications/publication_form.html'
    success_url = reverse_lazy('publications-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PublicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publications/publication_form.html'
    success_url = reverse_lazy('publications-list')

    def get_queryset(self):
        return Publication.objects.filter(user=self.request.user)


class PublicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Publication
    template_name = 'publications/publication_confirm_delete.html'
    success_url = reverse_lazy('publications-list')

    def get_queryset(self):
        return Publication.objects.filter(user=self.request.user)


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publications/publication_details.html'
    context_object_name = 'publication'

    def get_queryset(self):
        return Publication.objects.all()

    def get(self, request, pk, *args, **kwargs):
        publication = get_object_or_404(Publication, pk=pk)
        # Trier les versions par date de création en ordre décroissant
        versions = publication.versions.all().order_by('-created_at')

        # Récupérer le paramètre version_pk de la requête (s'il existe)
        version_pk = request.GET.get('version_pk')

        if version_pk:
            # Si version_pk est fourni, récupérer cette version spécifique
            current_version = get_object_or_404(PublicationVersion, pk=version_pk, publication=publication)
        else:
            # Sinon, utiliser la version actuelle de la publication
            current_version = publication.current_version

        return render(request, self.template_name, {
            'publication': publication,
            'current_version': current_version,
            'versions': versions
        })

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        try:
            return Publication.objects.get(pk=pk)
        except Publication.DoesNotExist:
            raise Http404("No Publication matches the given query.")


class AddPublicationVersionView(LoginRequiredMixin, View):
    form_class = PublicationForm

    def post(self, request, pk):
        publication = get_object_or_404(Publication, pk=pk)
        form = PublicationVersionForm(request.POST)
        if form.is_valid():
            version = form.save(commit=False)
            version.publication = publication  # Associer la version à la publication
            version.save()
            publication.current_version = version  # Mettre à jour la version actuelle de la publication
            publication.save()
            return redirect('publication-detail', pk=pk)
        return redirect('publication-detail', pk=pk)  # Si le formulaire n'est pas valide, retourner à la page détail


class PublicationVersionEditView(UpdateView):
    model = PublicationVersion
    form_class = PublicationVersionForm
    template_name = 'publications/publication_version_edit.html'  # votre template pour l'édition
    context_object_name = 'version'

    def get_object(self, queryset=None):
        # Récupérer le pk de la version depuis les paramètres de l'URL
        version_pk = self.kwargs['pk']
        # Retourner l'objet version
        return PublicationVersion.objects.get(pk=version_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter le publication_pk au contexte
        context['publication_pk'] = self.kwargs['publication_pk']
        context['formatted_publication_date'] = self.object.publication_date.strftime('%Y-%m-%d')
        return context
