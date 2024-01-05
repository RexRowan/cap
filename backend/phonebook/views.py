from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PhonebookSerializer
from .models import Phonebook

class PhonebookView(viewsets.ModelViewSet):
    serializer_class = PhonebookSerializer
    queryset = Phonebook.objects.all()

