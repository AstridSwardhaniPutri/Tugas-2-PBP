from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import return_json_id
from mywatchlist.views import return_XML_id



app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', return_json_id, name='return_json_id'),
    path('xml/<int:id>', return_XML_id, name='return_xml_id'),

]    
