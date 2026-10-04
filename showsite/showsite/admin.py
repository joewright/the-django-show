from django.contrib import admin

from showsite.models import Show, Venue


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("hidden",)


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ("day", "venue__name", "headliner", "support")
    list_filter = ("venue__name",)
    date_hierarchy = "day"
    list_select_related = ("venue",)
