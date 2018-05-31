from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', get_products, name="products"),
    url(r'^categories/([a-z]+)', get_cat_products, name="categories"),
    url(r'^lowest_price/', order_lowest, name="lowest"),
    url(r'^highest_price/', order_highest, name="highest"),
    url(r'^sort_az/', order_az, name="az"),
    url(r'^sort_za/', order_za, name="za"),
    url(r'^view_product/(\d+)', view_product, name="view_product"),
    
]