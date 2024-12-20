from django.urls import path
from .views import booking_view
 
urlpatterns = [
    path('book/', booking_view, name='booking_view'),
]