"""URL paths for Tournament App"""
from django.urls import path

from .views import (
    TourDetail,
    TourList,
)

urlpatterns = [
    path("", TourList.as_view(), name="tour_list"),
    path("tour/<str:slug>/", TourDetail.as_view(), name="tour_detail"),
]
