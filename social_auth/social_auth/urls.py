from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    # Url Entries for social auth
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Url Entries for django administration
    url('', include('django.contrib.auth.urls', namespace='auth')),

    # Url for the social networks
    url(r'^social_networks/', include('social_networks.urls', namespace='social_networks'))
)
