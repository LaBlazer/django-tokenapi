from django.conf.urls import url

from tokenapi.views import token
from tokenapi.views import token_new


urlpatterns = [
    url(r'^new$', token_new, name='api_token_new'),
    url(r'^(?P<token>.{24})/(?P<user>\d+)$', token, name='api_token'),
]
