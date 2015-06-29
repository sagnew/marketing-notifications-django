from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Subscriber(models.Model):
    phone_number = models.CharField(max_length=15)
    subscribed = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.phone_number, self.subscribed)
