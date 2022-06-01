from rest_framework import serializers
from .models import *


class CantonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canton
        fields = '__all__'


class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitor
        fields = ('username', 'first_name', 'last_name', 'email', 'url', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}



class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
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
