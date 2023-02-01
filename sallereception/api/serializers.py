from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class Type_FeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Fete
        fields = "__all__"


class Type_DecorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Decor
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
