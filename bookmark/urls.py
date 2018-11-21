from django.conf.urls import url
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark_app'

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<px>\d+)/$', BookmarkDV.as_view(), name='detail'),
]