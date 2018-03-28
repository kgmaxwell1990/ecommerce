from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', view_wishlist, name="view_wishlist") ,
    url(r'^add/$', add_to_wishlist, name="add_to_wishlist"),
    url(r'^remove_wishlist_item/(\d+)/$', remove_wishlist_item, name="remove_wishlist_item"),
]