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


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['first_name', 'last_name', 'username']
    search_fields = ['first_name', 'last_name', 'username']


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['name', 'address', 'canton']
    search_fields = ['name', 'address']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['name', 'description', 'add_date', 'place']
    search_fields = ['name', 'description', 'add_date']


class RateEventViewSet(viewsets.ModelViewSet):
    queryset = RateEvent.objects.all()
    serializer_class = RateEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['name']
    search_fields = ['name']


class RatePlaceViewSet(viewsets.ModelViewSet):
    queryset = RatePlace.objects.all()
    serializer_class = RatePlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
