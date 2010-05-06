"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

import ucsearch.views as views

class ViewSearchPageTest(TestCase):
    ''' How to test. Need sample solr running.
    '''

    def test_view_search_home(self):
        c = Client()
        response = c.get('/search')
        self.assertEqual(response.status_code, 301)
        response = c.get('/search/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/search/?q="polar bear"')
        self.assertEqual(response.status_code, 200)
