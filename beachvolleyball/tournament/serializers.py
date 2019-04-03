from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)
from .models import Tournament

class TournamentSerializer(HyperlinkedModelSerializer):
    """Serialize Tournament data"""

    class Meta:
        model = Tournament
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field":"slug",
                "view_name":"api-tour-detail",
            },
        }
