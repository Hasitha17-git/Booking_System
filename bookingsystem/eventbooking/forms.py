from django import forms
from .models import Event,Coupon,Booking
from django.core.exceptions import ValidationError

class BookingForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), label="Select Event")
    number_of_tickets = forms.IntegerField(min_value=1, label="Number of Tickets")
    coupon_code = forms.CharField(max_length=50, required=False, label="Coupon Code")
    # Custom Validation for the number of tickets
    def clean_number_of_tickets(self):
        number_of_tickets = self.cleaned_data.get('number_of_tickets')
        if number_of_tickets <= 0:
            raise ValidationError("Number of tickets must be a positive integer.")
        return number_of_tickets
    # Custom Validation for the coupon code
    def clean_coupon_code(self):
        code = self.cleaned_data.get('coupon_code')
        if code:
            try:
                Coupon.objects.get(code=code)
            except Coupon.DoesNotExist:
                raise ValidationError("Invalid coupon code.")
        return code