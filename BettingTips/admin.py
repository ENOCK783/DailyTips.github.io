from django.contrib import admin
from .models import Tip

# Customizing the Tip admin panel
@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('match', 'tip', 'odds', 'date')  # Columns to display in the admin list view
    list_filter = ('date',)  # Filters for the date field
    search_fields = ('match', 'tip')  # Searchable fields
    ordering = ('-date',)  # Order by most recent date by default

