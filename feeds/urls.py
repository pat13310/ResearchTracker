from django.urls import path
from .views import RSSFeedListView, RSSFeedCreateView, RSSFeedUpdateView, RSSFeedDeleteView

urlpatterns = [
    path('', RSSFeedListView.as_view(), name='rssfeed-list'),
    path('add/', RSSFeedCreateView.as_view(), name='rssfeed-add'),
    path('<int:pk>/edit/', RSSFeedUpdateView.as_view(), name='rssfeed-edit'),
    path('<int:pk>/delete/', RSSFeedDeleteView.as_view(), name='rssfeed-delete'),
]
