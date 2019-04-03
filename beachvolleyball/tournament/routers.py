from django.urls import path
from .views import (
    TournamentAPIList,
    TournamentAPIDetail,
)

urlpatterns = [
    path('', TournamentAPIList.as_view(), name='api-tour-list'),
    path(
        "tour/<str:slug>/",
        TournamentAPIDetail.as_view(),
        name='api-tour-detail',
        ),
]
