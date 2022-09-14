from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem
def show_catalog(request):
    cat_Item_Container= CatalogItem.objects.all()
    context = {
    'list_barang': cat_Item_Container,
    'nama': "Astrid",
    'NPM' :"2106707113"
    }
    return render(request, "katalog.html", context)
