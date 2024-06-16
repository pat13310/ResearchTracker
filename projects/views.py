import os

import django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import viewsets

from publications.models import Publication
from .forms import ProjectForm
from .models import Project
from serializers import ProjectSerializer

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ResearchTracker.settings')
# django.setup()


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Créer un projet'
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Modifier un projet'
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = Project.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        search_by = self.request.GET.get('search_by', 'title')
        if query:
            if search_by == 'title':
                queryset = queryset.filter(title__icontains=query)
            elif search_by == 'date':
                queryset = queryset.filter(start_date__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['root'] = "project"
        return context


class ProjectDashboardView(ListView):
    model = Project
    template_name = 'projects/project_dashboard.html'
    context_object_name = 'projects'


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')  # Redirige vers la liste des projets après suppression


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter les publications associées au projet
        project = self.get_object()
        context['publications'] = Publication.objects.filter(project=project)
        return context
