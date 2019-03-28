from django.shortcuts import render
from django.utils import timezone
from .models import Tournament

def tournament_list(request):
    tours = Tournament.objects.filter(event_date__lte=timezone.now()).order_by('event_date')
    return render(request, 'tournament/tournament_list.html', {'tours':tours})
