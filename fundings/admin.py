from django.contrib import admin

from fundings.models import Funding


# Register your models here.
@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'start_date', 'active', 'project')
    search_fields = ('name', 'amount', 'start_date', 'active','project')
