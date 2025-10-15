from django.contrib import admin
from .models import Ticket, Review

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "time_created")
    search_fields = ("title", "description")
    list_filter = ("time_created",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("headline", "user", "rating", "time_created")
    search_fields = ("headline", "body")
    list_filter = ("rating", "time_created")
