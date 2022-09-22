from django.shortcuts import render
from mywatchlist.models import ListFilm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    my_watchlist = ListFilm.objects.all()

    context = {
        'list_mywatchlist': my_watchlist,
        'nama': 'Astrid',
    }

    return render(request, "mywatchlist.html", context)

def show_xml (request):
    data = ListFilm.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json (request):
    data = ListFilm.objects.all()    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def return_json_id (request,pk=id):
    data = ListFilm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def return_XML_id (request,pk=id):
    data = ListFilm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

