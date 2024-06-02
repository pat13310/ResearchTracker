from django.urls import path
from .views import SimplifyTextView, SummarizeTextView, TranslateTextView

urlpatterns = [
    path('simplify/', SimplifyTextView.as_view(), name='simplify-text'),
    path('summarize/', SummarizeTextView.as_view(), name='summarize-text'),
    path('translate/', TranslateTextView.as_view(), name='translate-text'),
]
