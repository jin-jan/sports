from django.conf import settings
from django.db.models import (
    CharField,
    DateField,
    Model,
)
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone

class Tournament(Model):
    name = CharField(max_length=31)
    slug = AutoSlugField(
        max_length=31,
        unique_for_month="event_date",
        populate_from=["name"],
        help_text="A label for URL config.",)
    event_date = DateField()
    city = CharField(max_length=50)
    location = CharField(max_length=50)
    description = CharField(max_length=200)

    class Meta:
        get_latest_by = "event_date"
        ordering = ["-event_date"]
        verbose_name = "tournament post"

    def __str__(self):
        return self.name
