from django.urls import path, re_path
from api.views import *

urlpatterns = [
    path('collections/', create_collection),
    re_path(r'^update_capacity/(?P<collection_name>\w+)/', update_capacity),
    re_path(r'^collections/(?P<collection_name>\w+)/data/(?P<key>\w+)', get_data),
    re_path(r'^collections/(?P<collection_name>\w+)/data', put_data),
]
