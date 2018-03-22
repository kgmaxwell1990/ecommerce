from django.conf.urls import url
from .views import get_checkout

urlpatterns = [
    url(r'^$', get_checkout, name='checkout'),
]