from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Subscriber(models.Model):
    phone_number = models.CharField(max_length=15)
    subscribed = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.phone_number, self.subscribed)

    def handle_message(self, message_body):
        # Conditional logic to do different things based on the command from
        # the user
        if message_body == 'subscribe' or message_body == 'unsub':
            # If the user has elected to subscribe for messages, flip the bit
            # and indicate that they have done so.
            self.subscribed = message_body == 'subscribe'
            self.save()

            # Otherwise, our subscription has been updated
            response_message = 'You are now subscribed for updates.'
            if not self.subscribed:
                response_message = 'You have unsubscribed. Text "subscribe"' \
                                   ' to start receiving updates again.'
            return response_message
        else:
            return 'Sorry, we didn\'t understand that. available commands are' \
                   ': subscribe or unsubscribe'
