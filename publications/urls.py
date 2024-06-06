from django.urls import path

from publications.views import PublicationListView, PublicationCreateView, PublicationUpdateView, PublicationDeleteView, \
    PublicationDetailView

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('add/', PublicationCreateView.as_view(), name='publication-create'),
    path('edit/<int:pk>/', PublicationUpdateView.as_view(), name='publication-update'),
    path('delete/<int:pk>/', PublicationDeleteView.as_view(), name='publication-delete'),
    path('detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
]
