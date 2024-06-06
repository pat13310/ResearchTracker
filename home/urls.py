from django.urls import path

from home.views import HomeView
from publications.views import PublicationListView, PublicationCreateView, PublicationUpdateView, PublicationDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
