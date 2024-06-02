from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .models import Publication
from .forms import PublicationForm
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
