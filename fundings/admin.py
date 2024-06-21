from django.contrib import admin

from fundings.models import Funding


# Register your models here.
@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'start_date', 'end_date', 'project')
    search_fields = ('source', 'amount', 'start_date', 'end_date','project')
