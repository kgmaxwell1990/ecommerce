from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', view_wishlist, name="view_wishlist") ,
    url(r'^add/$', add_to_wishlist, name="add_to_wishlist"),
    url(r'^remove_wishlist_item/(\d+)/$', remove_wishlist_item, name="remove_wishlist_item"),
    url(r'^remove_all_wishlist_items/$', delete_all_wishlist_items, name="delete_all_wishlist_items"),
    url(r'^add_all_wishlist_items_to_cart/$', add_all_wishlist_items_to_cart, name="add_all_wishlist_items_to_cart"),
]