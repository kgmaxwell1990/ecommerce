from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', view_cart, name="view_cart") ,
    url(r'^add/$', add_to_cart, name="add_to_cart"),
    url(r'^delete_item/(\d+)/$', delete_item, name="delete_item"),
    url(r'^adjust_item/(\d+)/$', adjust_item, name="adjust_item") 
]