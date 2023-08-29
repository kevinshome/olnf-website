from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("artists/", views.artist_no_artist, name="artists"),
    path("directors/", views.directors_no_director, name="directors"),
    path("artists/<str:artist>/", views.artists_with_artist, name="artists_with_artist"),
    path("directors/<str:director>/", views.directors_with_director, name="directors_with_director"),
#    path("shop/", views.shop, name="shop"),
#    path("events/", views.events, name="events"),
#    path("contact/", views.contact, name="contact")
]