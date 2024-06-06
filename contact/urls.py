from django.urls import path

import contact.views

urlpatterns = [
    path('', contact.views.ContactUs.as_view(), name='contact'),
]