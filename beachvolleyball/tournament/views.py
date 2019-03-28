from django.shortcuts import render
from django.utils import timezone
from .models import Tournament

def tournament_list(request):
    tours = Tournament.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'tournament/tournament_list.html', {'tours':tours})
