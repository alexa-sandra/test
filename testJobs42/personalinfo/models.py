from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    birth_date = models.DateField()
    bio = models.TextField()
    email = models.EmailField(max_length=75)
    skype = models.CharField(max_length=40)
    jabber = models.CharField(max_length = 75)
    other_contacts = models.TextField()

    def _get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)