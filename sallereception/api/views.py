from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]


class Type_DecorViewSet(viewsets.ModelViewSet):
    queryset = Type_Decor.objects.all()
    serializer_class = Type_DecorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]


class Type_FeteViewSet(viewsets.ModelViewSet):
    queryset = Type_Fete.objects.all()
    serializer_class = Type_FeteSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]


# Create your views here.
