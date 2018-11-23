from django.conf.urls import url
from photo.views import *

app_name = 'photo_app'

urlpatterns = [
    # Example: /
    url(r'^$', AlbumLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),

    # Example: /album/(number)/
    url(r'^album/(?P<pk>\d)\d+/$', AlbumDV.as_view, name='album_detail'),

    # Example: /photo/(number)
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
]