from django.conf.urls import patterns, url, include
from accounts import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index),
    url(r'^accounts/', include('accounts.urls')),
)
