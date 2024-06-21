from django.contrib import admin

from publications.models import Publication


# Register your models here.
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors',  'doi')
    search_fields = ('title', 'authors', 'doi')
    site_title = 'Publications'
    site_header = 'Liste des publications'
