
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from django.utils import timezone

from .serializers import TournamentSerializer
from .models import Tournament

class TournamentApiList(ListAPIView):

    #return render(request, 'tournament/tournament_list.html', tour_json)
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

#def tournament_list(request):
    #return HttpResponse("Hello")
#    tours = Tournament.objects.filter(event_date__lte=timezone.now()).order_by('event_date')
#    return render(request, 'tournament/tournament_list.html', {'tours':tours})

class TournamentApiDetail(RetrieveAPIView):
    """Return JSON for single Tournament object"""
        #return render(request, 'tournament/tournament_detail.html', tour_json)
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    lookup_field = "slug"
