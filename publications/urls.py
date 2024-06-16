from django.urls import path

from publications.views import PublicationListView, PublicationCreateView, PublicationUpdateView, PublicationDeleteView, \
    PublicationDetailView, AddPublicationVersionView,  PublicationVersionEditView

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('add/', PublicationCreateView.as_view(), name='publication-create'),
    path('edit/<int:pk>/', PublicationUpdateView.as_view(), name='publication-update'),
    path('delete/<int:pk>/', PublicationDeleteView.as_view(), name='publication-delete'),
    path('detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('version/edit/<int:pk>/', PublicationUpdateView.as_view(), name='publication-version-edit'),
    path('<int:publication_pk>/versions/edit/<int:pk>/', PublicationVersionEditView.as_view(), name='publication-version-edit'),
    path('publication/<int:pk>/add-version/', AddPublicationVersionView.as_view(), name='publication-add-version'),
]
