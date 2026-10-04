import re

from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    Model,
)


class Venue(Model):
    name = CharField(blank=False)
    hidden = BooleanField(default=False)

    @classmethod
    def normalize_venue_name(cls, value: str):
        # remove leading (status) values, trim whitespaces
        value = re.sub(r"^\(.*?\)\s*", "", value)
        return value.strip()


class Show(Model):
    venue = ForeignKey(Venue, on_delete=CASCADE)
    headliner = CharField(blank=False)
    support = CharField(blank=False)
    day = DateField(blank=False)
