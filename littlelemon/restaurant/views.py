from django.shortcuts import render
from rest_framework.generics import ( ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView)
from . models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.

def index(request):
     return render(request, 'restaurant/index.html', {})

class MenuItemsView(ListCreateAPIView):
     permission_classes = [IsAuthenticatedOrReadOnly]
     queryset = MenuItem.objects.all()
     serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
     queryset = MenuItem.objects.all()
     serializer_class = MenuItemSerializer
     permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet (viewsets.ModelViewSet):
     queryset = Booking.objects.all()
     serializer_class = BookingSerializer
     permission_classes = [IsAuthenticated]

