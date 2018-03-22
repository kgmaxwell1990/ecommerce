from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from home.views import *
from products.views import get_products
from accounts import urls as account_urls
from products import urls as product_urls
from cart import urls as cart_urls
from reviews import urls as reviews_urls
from checkout import urls as checkout_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="home"),
    url(r'^accounts/', include(account_urls)),
    url(r'^products/', include(product_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^reviews/', include(reviews_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
