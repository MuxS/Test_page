from django.conf.urls import url
from blog.views import *
from . import views
from mysite.views import HomeView

app_name = 'blog_app'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    # Example: /
    url(r'^index/$', PostLV.as_view(), name='index'),

    # Example: /post/(same as /)
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # Example: /2018/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2018/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2018/nov/1
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    # Example: /search/
    url(r'^search/$', SearchFormView.as_view(), name='search'),

    # login
    url(r'^login/$', views.login, name='login'),

    # logout
    url('^logout/$', views.logout, name='logout'),

    # signup
    url(r'^signup/$', views.signup, name='signup'),
]
