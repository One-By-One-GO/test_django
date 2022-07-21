from django.urls import re_path, include
from .views import CreateMeeting, SelectMeeting
from rest_framework import routers
from .serializers import UserViewSet, MeetingViewSet, ReserveViewSet


urlpatterns = [
    re_path('^meeting', CreateMeeting.as_view(), name='meeting'),
    re_path('^selectmeeting', SelectMeeting.as_view(), name='selectmeeting'),
]