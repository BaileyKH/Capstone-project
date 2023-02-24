#define URL route for index() view
from django.urls import path
from . import views
from .views import index, home, BookingView, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('', home, name='home'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    #path('booking/', BookingView),
    path('api-token-auth/', obtain_auth_token),
]