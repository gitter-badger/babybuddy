# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^children/$', views.ChildList.as_view(), name='child-list'),
    url(r'^children/add/$', views.ChildAdd.as_view(), name='child-add'),
    url(r'^children/(?P<slug>[^/.]+)/$', views.ChildDetail.as_view(),
        name='child'),
    url(r'^children/(?P<slug>[^/.]+)/edit/$', views.ChildUpdate.as_view(),
        name='child-update'),
    url(r'^children/(?P<slug>[^/.]+)/delete/$', views.ChildDelete.as_view(),
        name='child-delete'),

    url(r'^changes/$', views.DiaperChangeList.as_view(),
        name='diaperchange-list'),
    url(r'^changes/add/$', views.DiaperChangeAdd.as_view(),
        name='diaperchange-add'),
    url(r'^changes/(?P<pk>[0-9]+)/$', views.DiaperChangeUpdate.as_view(),
        name='diaperchange-update'),
    url(r'^changes/(?P<pk>[0-9]+)/delete/$',
        views.DiaperChangeDelete.as_view(), name='diaperchange-delete'),

    url(r'^feedings/$', views.FeedingList.as_view(), name='feeding-list'),
    url(r'^feedings/add/$', views.FeedingAdd.as_view(), name='feeding-add'),
    url(r'^feedings/(?P<pk>[0-9]+)/$', views.FeedingUpdate.as_view(),
        name='feeding-update'),
    url(r'^feedings/(?P<pk>[0-9]+)/delete/$', views.FeedingDelete.as_view(),
        name='feeding-delete'),

    url(r'^notes/$', views.NoteList.as_view(), name='note-list'),
    url(r'^notes/add/$', views.NoteAdd.as_view(), name='note-add'),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.NoteUpdate.as_view(),
        name='note-update'),
    url(r'^notes/(?P<pk>[0-9]+)/delete/$', views.NoteDelete.as_view(),
        name='note-delete'),

    url(r'^sleep/$', views.SleepList.as_view(), name='sleep-list'),
    url(r'^sleep/add/$', views.SleepAdd.as_view(), name='sleep-add'),
    url(r'^sleep/(?P<pk>[0-9]+)/$', views.SleepUpdate.as_view(),
        name='sleep-update'),
    url(r'^sleep/(?P<pk>[0-9]+)/delete/$', views.SleepDelete.as_view(),
        name='sleep-delete'),

    url(r'^timers/$', views.TimerList.as_view(), name='timer-list'),
    url(r'^timer/add/$', views.TimerAdd.as_view(), name='timer-add'),
    url(r'^timer/add/quick/$', views.TimerAddQuick.as_view(),
        name='timer-add-quick'),
    url(r'^timer/(?P<pk>[0-9]+)/$', views.TimerDetail.as_view(),
        name='timer-detail'),
    url(r'^timer/(?P<pk>[0-9]+)/edit/$', views.TimerUpdate.as_view(),
        name='timer-update'),
    url(r'^timer/(?P<pk>[0-9]+)/delete/$', views.TimerDelete.as_view(),
        name='timer-delete'),
    url(r'^timer/(?P<pk>[0-9]+)/stop/$', views.TimerStop.as_view(),
        name='timer-stop'),
    url(r'^timer/(?P<pk>[0-9]+)/restart/$', views.TimerRestart.as_view(),
        name='timer-restart'),

    url(r'^tummy-time/$', views.TummyTimeList.as_view(),
        name='tummytime-list'),
    url(r'^tummy-time/add/$', views.TummyTimeAdd.as_view(),
        name='tummytime-add'),
    url(r'^tummy-time/(?P<pk>[0-9]+)/$', views.TummyTimeUpdate.as_view(),
        name='tummytime-update'),
    url(r'^tummy-time/(?P<pk>[0-9]+)/delete/$',
        views.TummyTimeDelete.as_view(), name='tummytime-delete'),

    url(r'^weight/$', views.WeightList.as_view(), name='weight-list'),
    url(r'^weight/add/$', views.WeightAdd.as_view(), name='weight-add'),
    url(r'^weight/(?P<pk>[0-9]+)/$', views.WeightUpdate.as_view(),
        name='weight-update'),
    url(r'^weight/(?P<pk>[0-9]+)/delete/$', views.WeightDelete.as_view(),
        name='weight-delete'),
]
