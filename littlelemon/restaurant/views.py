from django.shortcuts import render
from .models import Menu, Booking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

class BookingView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
#class MenuView(generics.ListCreateView):
    #def post(self, request):
        #serializer = MenuSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response({"status": "Success", "data": serializer.data})
        
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
