from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from home.views import *
from accounts import urls as account_urls
from products import urls as product_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="home"),
    url(r'^accounts/', include(account_urls)),
    url(r'^products/', include(product_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
