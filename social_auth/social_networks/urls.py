from django.conf.urls import patterns, include, url
from django.contrib import admin
from social_networks import views

urlpatterns = patterns('',

    # Url for the social networks
    url(r'^$', views.SocialTestView.as_view(), name='social_auth')
)