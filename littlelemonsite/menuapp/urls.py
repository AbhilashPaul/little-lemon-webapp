from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.menu, name='menu'), 
    path('salads', views.menu_salads, name='salad menu'), 
] 