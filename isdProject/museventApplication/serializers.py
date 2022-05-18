from rest_framework import serializers
from .models import *


class CantonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Canton
        fields = '__all__'


class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitor
        fields = ('username', 'first_name', 'last_name', 'email', 'url')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class RateEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RateEvent
        fields = '__all__'


class RatePlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RatePlace
        fields = '__all__'


class ParticipationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participation
        fields = '__all__'
