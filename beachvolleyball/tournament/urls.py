from django.urls import path
from .views import (
    TournamentApiList,
    TournamentApiDetail,
)

urlpatterns = [
    path('', TournamentApiList.as_view(), name='api-tour-list'),
    path(
        "tour/<str:slug>/",
        TournamentApiDetail.as_view(),
        name='api-tour-detail',
        ),
]
