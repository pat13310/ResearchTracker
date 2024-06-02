from django.urls import path
from .views import CreateDOIView, PublicationDetailView

urlpatterns = [
    path('create/', CreateDOIView.as_view(), name='create-doi'),
    path('publication/<str:doi>/', PublicationDetailView.as_view(), name='publication-detail'),
]
