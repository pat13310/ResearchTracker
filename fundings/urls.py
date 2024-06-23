from django.urls import path

from fundings.views import FundingListView, FundingCreateView

urlpatterns = [
    path('list/', FundingListView.as_view(), name='funding-list'),
    path('create/', FundingCreateView.as_view(), name='funding-create'),
]
