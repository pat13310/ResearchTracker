from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, \
    ProjectDetailView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('list/', ProjectListView.as_view(), name='project-list'),
    path('add/', ProjectCreateView.as_view(), name='project-create'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('edit/<int:pk>/', ProjectUpdateView.as_view(), name='project-edit'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'),
    path("dashboard/", ProjectListView.as_view(), name="project-dashboard"),
]
