# cal/urls.py

from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^calendar/$', views.CalendarView.as_view(), name="calendar"),
    url(r'^index/$', views.index, name="index"),
    # url(r'^$', views.CalendarView.as_view, name='cal'),
]