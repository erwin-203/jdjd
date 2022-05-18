from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.


class CantonViewSet(viewsets.ModelViewSet):
    queryset = Canton.objects.all()
    serializer_class = CantonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RateEventViewSet(viewsets.ModelViewSet):
    queryset = RateEvent.objects.all()
    serializer_class = RateEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RatePlaceViewSet(viewsets.ModelViewSet):
    queryset = RatePlace.objects.all()
    serializer_class = RatePlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
