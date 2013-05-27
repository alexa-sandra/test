# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test.client import Client

from django.utils import unittest
from models import Person


class PersonTestCase(unittest.TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            last_name=u'Сидоров',
            first_name=u'Александр',
            birth_date = '1966-12-12',
            bio = u'Выдающийся украинский спортсмен, который родился еще тра-ля-ля',
            email = 'sidodovmail@mail.ru',
            skype = 'sidorovskype',
            jabber = 'sidodovmail@jabber.ru',
            other_contacts = u'ну а здесь телефоны для связи и всякие разные другие контакты',
        )
        self.client = Client()
        
    def test__unicode__(self):
        person = u"%s %s" % (self.person.last_name,
                                self.person.first_name)
        self.assertEqual(unicode(self.person), person)
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        

