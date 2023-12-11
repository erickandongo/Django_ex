from django.urls import path 

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("objectives", views.objectives, name="objectives-page"),
    path("objectives/<slug:slug>", views.objectives_details, name="objectives-details-page")
]
