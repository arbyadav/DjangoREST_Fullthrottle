
import factory
import factory.django
from django.utils import timezone
from django.db import models
# Create your models here.


class UsersD(models.Model):

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=500, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)

    def __str__(self):
        # to modify look in db objects
        return f"{self.name}"


class ActivityPeriod(models.Model):
    user = models.ForeignKey(UsersD, on_delete=models.CASCADE)
    activityname = models.CharField(max_length=100, blank=False)
    playedOn = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['activityname']

    def __str__(self):
        return self.activityname


class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.Faker('email')
    address = factory.Faker('address')
    phone_number = factory.Faker('msisdn')

    class Meta:
        model = UsersD
