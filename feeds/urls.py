from django.urls import path
from .views import RSSFeedListView, RSSFeedCreateView, RSSFeedUpdateView, RSSFeedDeleteView, RSSFeedDetailView

urlpatterns = [
    path('', RSSFeedListView.as_view(), name='rss-feed-list'),
    path('add/', RSSFeedCreateView.as_view(), name='rss-feed-add'),
    path('<int:pk>/edit/', RSSFeedUpdateView.as_view(), name='rss-feed-edit'),
    path('<int:pk>/delete/', RSSFeedDeleteView.as_view(), name='rss-feed-delete'),
    path('detail/<int:pk>/', RSSFeedDetailView.as_view(), name='rss-feed-detail'),
]
