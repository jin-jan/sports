"""Views for Tournament App"""
from django.shortcuts import get_object_or_404, render
#from django.views.generic import (
#    DetailView,
#    ListView,
#)
from django.views import View
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .serializers import TournamentSerializer
from .models import Tournament

class TourList(View):
    """Display a list of tournaments"""

    def get(self,request):
        """Render an HTML template of a list of tournaments"""
        tour_list = Tournament.objects.all()
        context = {"tour_list":tour_list}
        return render(request, "tournament/list.html", context)

class TourDetail(View):
    """Display a single Tournament"""

    def get(self, request, slug):
        """Render an HTML template of a tournament"""
        tour = get_object_or_404(Tournament, slug=slug)
        context = {"tour":tour}
        return render(request, "tournament/detail.html", context)

class TournamentAPIList(ListAPIView):
    """Return JSON for multiple Tournament objects"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class TournamentAPIDetail(RetrieveAPIView):
    """Return JSON for single tournament object"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    lookup_field = "slug"
