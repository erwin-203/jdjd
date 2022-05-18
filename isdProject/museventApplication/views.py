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
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = '__all__'


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
<<<<<<< HEAD
    filter_fields = ['first_name', 'last_name', 'username']
    search_fields = ['first_name', 'last_name', 'username']
=======
    filter_fields = '__all__'
>>>>>>> a55fbc1d689557a97c5726ec3ec8815e84c6d0c4


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
<<<<<<< HEAD
    filter_fields = ['name', 'address']
    search_fields = ['name', 'address']
=======
    filter_fields = '__all__'
>>>>>>> a55fbc1d689557a97c5726ec3ec8815e84c6d0c4


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
<<<<<<< HEAD
    filter_fields = ['name', 'description', 'add_date']
    search_fields = ['name', 'description', 'add_date']
=======
    filter_fields = '__all__'
>>>>>>> a55fbc1d689557a97c5726ec3ec8815e84c6d0c4


class RateEventViewSet(viewsets.ModelViewSet):
    queryset = RateEvent.objects.all()
    serializer_class = RateEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
<<<<<<< HEAD
    filter_fields = ['name']
    search_fields = ['name']
=======
    filter_fields = '__all__'
>>>>>>> a55fbc1d689557a97c5726ec3ec8815e84c6d0c4


class RatePlaceViewSet(viewsets.ModelViewSet):
    queryset = RatePlace.objects.all()
    serializer_class = RatePlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = '__all__'


class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = '__all__'
