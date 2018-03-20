from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', get_products, name="products"),
]