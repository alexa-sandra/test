# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test.client import Client

from django.utils import unittest
from personalinfo.models import Person


class PersonTestCase(unittest.TestCase):
    """
    Test for model Person and main page
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        person = Person.objects.latest('id')
        self.find(str(person.first_name))
        self.find(str(person.last_name))
        self.find(str(person.birth_date.strftime("%d.%m.%Y")))
        self.find(str(person.bio))
        self.find(str(person.email))
        self.find(str(person.jabber))
        self.find(str(person.skype))
        

class TestEditForm(unittest.TestCase):
    """
    Test edit form
    """
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get('login')
        self.assertEqual(response.status_code, 200)

    def test_edit_form(self):
        user = User.objects.get(pk=1)
        # User not logged in
        response = self.client.get('edit')
        self.assertEqual(response.status_code, 403)

        self.client.login(username=user.username, password='admin')

        # Valid user
        response = self.client.get('edit')
        self.assertEqual(response.status_code, 200)

        #Form
        new_data = Person.objects.values().get(id=1)
        new_data['birth_date'] = '1987-12-13'

        self.client.post('edit', data=new_data)
        response = self.client.get('edit')
        self.assertContains(response, '')


