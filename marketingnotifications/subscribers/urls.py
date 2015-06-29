from django.conf.urls import url

from subscribers import views

urlpatterns = [
    url(r'^message/', views.message, name='message'),
]
