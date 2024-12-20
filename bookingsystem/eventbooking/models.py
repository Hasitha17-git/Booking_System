from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    price_per_ticket = models.DecimalField(max_digits=10, decimal_places=2)
 
    def __str__(self):
        return self.name
 
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 10.00 for 10%
 
    def __str__(self):
        return self.code
 
class Booking(models.Model):
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    number_of_tickets = models.PositiveIntegerField()
    price_per_ticket = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking for {self.event_name.name} ({self.number_of_tickets} tickets) - Total: ${self.total_price}"