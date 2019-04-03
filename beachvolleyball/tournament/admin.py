from django.contrib import admin
from .models import Tournament

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):

    list_display = ("name", "slug", "event_date")
    prepopulated_fields = {"slug": ("name",)}
