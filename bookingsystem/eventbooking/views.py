from django.shortcuts import render
from django.db import models
from django import forms
from eventbooking.forms import BookingForm
from .models import Coupon,Event,Booking
def booking_view(request):
    total_price = None
    discount = 0
    form = BookingForm(request.POST or None) # Creating form instance
 
    if request.method == "POST" and form.is_valid():
        event = form.cleaned_data['event']
        number_of_tickets = form.cleaned_data['number_of_tickets']
        coupon_code = form.cleaned_data.get('coupon_code')
 
        # Calculate the price per ticket
        price_per_ticket = event.price_per_ticket
 
        # Apply coupon discount if applicable
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code)
                discount = coupon.discount_percentage / 100
            except Coupon.DoesNotExist:
                discount = 0
 
        total_price = number_of_tickets * price_per_ticket * (1 - discount)
 
        # Save the booking
        Booking.objects.create(
            event_name=event,
            number_of_tickets=number_of_tickets,
            price_per_ticket=price_per_ticket,
            total_price=total_price
        )
 
        return render(request, "booking_success.html", {"total_price": total_price, "booking": Booking.objects.last(), "applied_coupon": coupon if coupon_code else None}) #Render the template with context
 
    coupons = Coupon.objects.all()
    return render(request, "booking_form.html", {"form": form, "total_price": total_price, "coupons": coupons})
