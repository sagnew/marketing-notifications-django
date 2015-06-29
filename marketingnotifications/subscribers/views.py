from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from subscribers.models import Subscriber

from twilio import twiml


@csrf_exempt
def message(request):
    phone_number = request.POST['From']

    try:
        sub = Subscriber.objects.get(phone_number=phone_number)
        return handle_message(sub)
    except Subscriber.DoesNotExist:
        # Create a subscriber with this phone number if one does not exist.
        new_subscriber = Subscriber(phone_number=phone_number)
        new_subscriber.save()
        response = twiml.Response()
        response.message('Thanks for contacting us! Text "subscribe" to '
                         'receive updates via text message.')
        return HttpResponse(response.toxml(), content_type='text/xml')


def handle_message(sub):
    return HttpResponse()
