import logging

import requests
from django.core.management.base import BaseCommand, CommandError
from showsite.models import Show, Venue

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import show data"

    def add_arguments(self, parser):
        parser.add_argument("--no-cache", type=bool, default=False, required=False)

    def handle(self, *args, **options):
        try:
            response = requests.get("https://atlshows.neocities.org/all-shows.json")
            data = response.json()
            venues = set()
            [venues.add(Venue.normalize_venue_name(entry["venue"])) for entry in data]
            # remove any venues that start with `http`
            venues = {venue for venue in venues if not venue.startswith("http")}
            venue_pks_by_name = {}
            # save all venues
            for venue_name in venues:
                venue, created = Venue.objects.get_or_create(name=venue_name)
                if created:
                    logger.info("Created new venue: %s", venue_name)
                venue_pks_by_name[venue_name] = venue.pk
            # save all shows
            for entry in data:
                venue_name = Venue.normalize_venue_name(entry["venue"])
                venue_pk = venue_pks_by_name.get(venue_name)
                if not venue_pk:
                    continue
                support = entry.get("support") or ""
                date_value = entry["date"]
                # parse date from '2026-10-02 (Fri)'
                date_value = date_value.split(" ")[0]
                Show.objects.get_or_create(
                    venue_id=venue_pk,
                    headliner=entry["headliner"],
                    support=support,
                    day=date_value,
                )
        
        except Exception:
            logger.exception("Command failed")
            raise CommandError("Command failed")
