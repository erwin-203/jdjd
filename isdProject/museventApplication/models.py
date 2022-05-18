from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from museventApplication.managers import VisitorManager
from museventProject import settings


class Canton(models.Model):
    name = models.CharField(max_length=64)


class Visitor(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

    #objects = VisitorManager()

    #USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['email', 'password']

    #@receiver(post_save)
    #def user_is_created(self, instance, created, **kwargs):
    #    if created:
    #        Visitor.objects.create(user=instance)
    #    else:
    #        instance.profile.save()


class Place(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    npa = models.IntegerField(max_length=5)
    date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    canton = models.ForeignKey(Canton, on_delete=models.DO_NOTHING)


class Event(models.Model):
    name = models.CharField(max_length=64)
    add_date = models.DateTimeField()
    description = models.CharField(max_length=256)
    max_participants = models.IntegerField(max_length=5)
    event_date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)


class RateEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    rate = models.IntegerField(max_length=1)
    comment = models.TextField(max_length=256)
    datetime = models.DateTimeField()


class RatePlace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING)
    rate = models.IntegerField(max_length=1)
    comment = models.TextField(max_length=256)
    datetime = models.DateTimeField()


class Participation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    inscription_date = models.DateTimeField()
