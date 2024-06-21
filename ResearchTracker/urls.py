"""
URL configuration for ResearchTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

from ResearchTracker import settings
from dashboard import views as dashboard_views
from home import views as home_views

# router = DefaultRouter()
# router.register(r'projets', ProjetViewSet)
# router.register(r'publications', PublicationViewSet)
# router.register(r'collaborateurs', CollaborateurViewSet)
# router.register(r'financements', FinancementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dashboard', dashboard_views.dashboard, name='dashboard'),
    path('projets/', include('projects.urls')),
    path('publications/', include('publications.urls')),
    # path('', include('collaborators.urls')),
    # path('', include('fundings.urls')),
    # path('', include('reports.urls')),
    # path('', include('notifications.urls')),
    path('auth/', include('authentication.urls')),
    path('profile/', include('userprofile.urls')),
    path('ia/', include('summarizer.urls')),
    path('api/doi', include('api.urls')),
    path('feeds/', include('feeds.urls')),
    path('contact/', include('contact.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),

]

# handler404 = 'ResearchTracker.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.index_title="ResearchTracker"
admin.site.site_header="Admin ResearchTracker"