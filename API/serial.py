from rest_framework import serializers
from .models import UsersD, ActivityPeriod


class UsersDSerial(serializers.ModelSerializer):

    class Meta:
        model = UsersD
        fields = '__all__'


class ActivitySerial(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = '__all__'
