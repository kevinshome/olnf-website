from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Member

def index(request: HttpRequest):
    return HttpResponse("GET /")

def home(request: HttpRequest):
    return HttpResponse("GET /home")

# /artists
def artist_no_artist(request: HttpRequest):
    return HttpResponse("GET /artists")

# /artists/<artist>
def artists_with_artist(request: HttpRequest, artist: str): # use models.Member
    artist_filter = Member.objects.filter(name=artist)
    if len(artist_filter) == 0:
        return HttpResponse("404 Not Found", status=404)
    return HttpResponse(f"GET /artists/{artist}") # show list of all artists

# /directors
def directors_no_director(request: HttpRequest):
    return HttpResponse("GET /directors")

# /directors/<director>
def directors_with_director(request: HttpRequest, director: str): # use models.Member
    director_filter = Member.objects.filter(name=director)
    if len(director_filter) == 0:
        return HttpResponse("404 Not Found", status=404)
    return HttpResponse(f"GET /directors/{director}") # show list of all directors

def shop(request: HttpRequest): # TODO: FUTURE
    return HttpResponse("GET /shop")

def events(request: HttpRequest): # TODO: FUTURE
    return HttpResponse("GET /events")

def contact(request: HttpRequest): # TODO: FUTURE
    return  HttpResponse("GET /contact")
