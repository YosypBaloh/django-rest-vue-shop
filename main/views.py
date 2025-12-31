from django.shortcuts import render
from .serializers import ItemSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Item


class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
