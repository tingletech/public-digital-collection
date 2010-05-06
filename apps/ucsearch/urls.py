from django.conf.urls.defaults import *
from ucsearch.views import get_search_page

urlpatterns = patterns('',
        url(r'.*', get_search_page, name='get_search_page'),
        #url(r'^/q=(?P<query>.+)',  view_search_page, name='view_search_page'),
        #url(r'^(?P<query>.+)',  view_search_page, name='view_search_page'),
)

