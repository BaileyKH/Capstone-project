from rest_framework import serializers
from .models import Menu, Booking

#class UserSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = User
        #fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    model = Booking
    fields = '__all__'
    
#class MenuItemSerializer(serializers.ModelSerializer):
    #model = Menu
    #fields = '__all__'