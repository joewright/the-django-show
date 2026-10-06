from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path

from showsite.models import Show, Venue


# Simple admin, customizable field and filter selection
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("hidden",)


# Adding a custom URL and view to a model admin
@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ("day", "venue__name", "headliner", "support")
    list_filter = ("venue__name",)
    date_hierarchy = "day"
    list_select_related = ("venue",)
    ordering = ("day",)

    def get_urls(self):
        urls = super().get_urls()
        prefix = f"{self.model._meta.app_label}_{self.model._meta.model_name}"
        return [
            path(
                "download/",
                self.admin_site.admin_view(self.download_view),
                name=f"{prefix}_download",
            )
        ] + urls

    def download_view(self, request: HttpRequest):
        """Export all Show objects as JSON"""
        shows = Show.objects.all()
        response = HttpResponse(content_type="application/json")
        response["Content-Disposition"] = "attachment; filename=shows.json"
        response.write("[")
        first = True
        for show in shows.iterator():
            if not first:
                response.write(",")
            response.write(show.to_json())
            first = False
        response.write("]")
        return response


# Standalone custom page
def my_url_view(request: HttpRequest):
    # gather admin context
    context = dict(
        **admin.site.each_context(request),
    )
    # render my_custom_page.html
    return render(request, "my_custom_page.html", context)


my_url_view.short_description = "My URL View"


# include the view in the admin site urls
original_get_urls = admin.site.get_urls


def get_urls():
    urls = [path("my-url/", admin.site.admin_view(my_url_view), name="my_url")]
    return urls + original_get_urls()


admin.site.get_urls = get_urls
