from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
url(r'signup', signup_view),
    url(r'login', login_view),
    url(r'feed', feed),
    url(r'^post', post_view, name='post'),
    url('like/', like_view),
    url('comment/', comment_view),
]
