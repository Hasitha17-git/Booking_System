from django.contrib import admin
from .models import Event,Coupon,Booking
# Register your models here.
admin.site.register(Event)
admin.site.register(Coupon)
admin.site.register(Booking)